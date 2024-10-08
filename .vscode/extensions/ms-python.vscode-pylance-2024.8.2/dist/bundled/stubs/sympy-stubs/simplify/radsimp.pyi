from typing import Any

from sympy.core.add import Add
from sympy.series.order import Order

def collect(expr, syms, func=..., evaluate=..., exact=..., distribute_order_term=...): ...
def rcollect(expr, *vars): ...
def collect_sqrt(expr, evaluate=...) -> tuple[tuple[Any | Order, ...], int]: ...
def collect_abs(expr): ...
def collect_const(expr, *vars, Numbers=...) -> Add | Order: ...
def radsimp(expr, symbolic=..., max_terms=...): ...
def rad_rationalize(num, den) -> tuple[Any, Any]: ...
def fraction(expr, exact=...) -> tuple[Any | Order, Any | Order]: ...
def numer(expr) -> Order: ...
def denom(expr) -> Order: ...
def fraction_expand(expr, **hints): ...
def numer_expand(expr, **hints): ...
def denom_expand(expr, **hints): ...

expand_numer = ...
expand_denom = ...
expand_fraction = ...

def split_surds(expr) -> tuple[Any, Any | Order, Any | Order]: ...
