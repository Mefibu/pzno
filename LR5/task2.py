import sympy as sp

# Найти все решения уравнения e^x - e^(-x) = 2
x = sp.Symbol('x')
equation = sp.E**x - sp.E**(-x) - 2
solutions = sp.solve(equation, x)
print(f'Решения уравнения e^x - e^(-x) = 2: {solutions}')