import ast
from collections import deque
from contextlib import suppress
from functools import partial
from pathlib import Path
from typing import Callable, Iterator, List, NamedTuple, Optional, Tuple, Type, TypeVar

import astroid

from .._stub import EXTENSION, StubFile, StubsManager


T = TypeVar('T', bound=Type)
N = Tuple[Type[T], Type[T]]


class TOKENS:
    ASSERT: N[ast.Assert] = (ast.Assert, astroid.Assert)
    ATTR: N[ast.Attribute] = (ast.Attribute, astroid.Attribute)
    BIN_OP: N[ast.BinOp] = (ast.BinOp, astroid.BinOp)
    CALL: N[ast.Call] = (ast.Call, astroid.Call)
    COMPARE: N[ast.Compare] = (ast.Compare, astroid.Compare)
    GLOBAL: N[ast.Global] = (ast.Global, astroid.Global)
    NONLOCAL: N[ast.Nonlocal] = (ast.Nonlocal, astroid.Nonlocal)
    RAISE: N[ast.Raise] = (ast.Raise, astroid.Raise)
    RETURN: N[ast.Return] = (ast.Return, astroid.Return)
    YIELD: N[ast.Yield] = (ast.Yield, astroid.Yield)


class Token(NamedTuple):
    line: int
    col: int
    value: Optional[object] = None
    marker: Optional[str] = None  # marker name or error message


def traverse(body: List) -> Iterator:
    for expr in body:
        if isinstance(expr, ast.AST):
            yield from _traverse_ast(expr)
        else:
            yield from _traverse_astroid(expr)


def _traverse_ast(node: ast.AST) -> Iterator[ast.AST]:
    todo = deque([node])
    while todo:
        node = todo.popleft()
        if isinstance(node, ast.Try):
            for h in node.handlers:
                todo.extend(h.body)
            todo.extend(node.orelse)
            todo.extend(node.finalbody)
        else:
            todo.extend(ast.iter_child_nodes(node))
            yield node


def _traverse_astroid(node: astroid.NodeNG) -> Iterator[astroid.NodeNG]:
    todo = deque([node])
    while todo:
        node = todo.popleft()
        if isinstance(node, astroid.TryExcept):
            for h in node.handlers:
                todo.extend(h.body)
            todo.extend(node.orelse)
        else:
            todo.extend(node.get_children())
            yield node


def get_name(expr) -> Optional[str]:
    if isinstance(expr, ast.Name):
        return expr.id
    if isinstance(expr, astroid.Name):
        return expr.name

    if isinstance(expr, astroid.Attribute):
        left = get_name(expr.expr)
        if left is None:
            return None
        return left + '.' + expr.attrname
    if isinstance(expr, ast.Attribute):
        left = get_name(expr.value)
        if left is None:
            return None
        return left + '.' + expr.attr

    return None


def get_full_name(expr: astroid.NodeNG) -> Tuple[str, str]:
    if expr.parent is None:
        return '', expr.name

    if type(expr.parent) is astroid.Module:
        return expr.parent.qname(), expr.name

    if type(expr.parent) in (astroid.FunctionDef, astroid.UnboundMethod):
        module_name, func_name = get_full_name(expr=expr.parent)
        return module_name, func_name + '.' + expr.name

    if type(expr.parent) is astroid.ClassDef:
        module_name, class_name = get_full_name(expr=expr.parent)
        return module_name, class_name + '.' + expr.name

    path, _, func_name = expr.qname().rpartition('.')
    return path, func_name


def infer(expr) -> Tuple[astroid.NodeNG, ...]:
    if not isinstance(expr, astroid.NodeNG):
        return tuple()
    with suppress(astroid.exceptions.InferenceError, RecursionError):
        guesses = expr.infer()
        if guesses is astroid.Uninferable:  # pragma: no cover
            return tuple()
        return tuple(g for g in guesses if repr(g) != 'Uninferable')
    return tuple()


def get_stub(
    module_name: Optional[str],
    expr: astroid.FunctionDef,
    stubs: StubsManager,
) -> Optional[StubFile]:
    if not module_name:
        return None
    stub = stubs.get(module_name)
    if stub is not None:
        return stub

    module = _get_module(expr=expr)
    if module is None or module.file is None:
        return None  # pragma: no coverage
    path = Path(module.file).with_suffix(EXTENSION)
    if not path.exists():
        return None
    return stubs.read(path=path)


def _get_module(expr: astroid.NodeNG) -> Optional[astroid.Module]:
    if type(expr) is astroid.Module:
        return expr
    if expr.parent is None:
        return None
    return _get_module(expr.parent)


class Extractor:
    __slots__ = ('handlers', )

    def __init__(self):
        self.handlers = dict()

    def _register(self, types: Tuple[type], handler: Callable) -> Callable:
        for tp in types:
            # it's here to have `getattr` to get nodes from `ast` module
            # that are available only in some Python versions.
            if tp is None:
                continue  # pragma: no coverage
            self.handlers[tp] = handler
        return handler

    def register(self, *types):
        return partial(self._register, types)

    def handle(self, expr, **kwargs):
        handler = self.handlers.get(type(expr))
        if handler is None:
            return
        token = handler(expr=expr, **kwargs)
        if token is None:
            return
        if type(token) is Token:
            yield token
            return
        yield from token

    def __call__(self, body: List, **kwargs) -> Iterator[Token]:
        for expr in traverse(body=body):
            yield from self.handle(expr=expr, **kwargs)
