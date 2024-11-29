import sympy as sp

# Найти первообразную функции f(x) = (x^2 - 1) / (x^2 + 5x)
x = sp.Symbol('x')
f_x = (x**2 - 1) / (x**2 + 5*x)
a = sp.integrate(f_x, x)
print(a)
b = (a).diff().together().simplify()
print(b)

