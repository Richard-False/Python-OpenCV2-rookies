def T10(f, a, b):
    """
    使用梯形法计算积分 ∫_a^b f(x) dx，
    分成 10 个小区间。
    """
    n = 10
    h = (b - a) / n
    s = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        s += f(a + i * h)
    return h * s

def M10(f, a, b):
    """
    使用中点法计算积分 ∫_a^b f(x) dx，
    分成 10 个小区间，取每个区间中点作为高度。
    """
    n = 10
    h = (b - a) / n
    s = 0
    for i in range(n):
        mid = a + (i + 0.5) * h
        s += f(mid)
    return h * s

def S10(f, a, b):
    """
    使用辛普森法计算积分 ∫_a^b f(x) dx，
    将区间分成 10 个小区间（n 必须为偶数）。
    """
    n = 10
    if n % 2 != 0:
        raise ValueError("n 必须为偶数，才能使用辛普森法")
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        if i % 2 == 0:
            s += 2 * f(a + i * h)
        else:
            s += 4 * f(a + i * h)
    return h * s / 3

from math import pi,sin,cos,tan # type: ignore
import sympy
from sympy import pi,sin,cos,tan
x = sympy.symbols('x')
def f(x):
    return  39*sin(x)

a=0
b=pi
print(T10(f(x), a, b))
print(M10(f(x), a, b))
print(S10(f(x), a, b))