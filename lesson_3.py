from sympy import *
from math import inf
import time
# Первый вариант пошустрее, но они не сильно отличаются друг от друга в целом.
start = time.time()
n = oo
b = n / factorial(n) ** (1 / n)
print(b)
print(time.time() - start)
# Читала, что функция limit не работает при стремлении предела к бесконечности.
# Но здесь результат выдает, хоть и медленнее.
start = time.time()
x = symbols("x")
exp = x / factorial(x) ** (1 / x)
b = exp.subs(x, oo)
z = limit(b, x, oo)
print(z)
print(time.time() - start)


