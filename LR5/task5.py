import sympy as sp

# Вычислить правосторонний предел
x = sp.Symbol('x')
right_limit = sp.limit(sp.acos(1 - x), x, 1, dir='+')
print(f'Правосторонний предел: {right_limit}')
