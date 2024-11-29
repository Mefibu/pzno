import sympy as sp

# Вычислить определенный интеграл от 0 до 2
x = sp.Symbol('x')
integral_result = sp.integrate(x**2 * sp.exp(x), (x, 0, 1))
print(f'Определенный интеграл от 0 до 2: {integral_result}')