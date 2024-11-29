import sympy as sp

# Найти предел
m, n, x = sp.symbols('m n x')
limit_expr = ((1 + m*x)**n - (1 + n*x)**m) / x**2
limit_result = sp.limit(limit_expr, x, 0)
print(f'Предел выражения: {limit_result}')