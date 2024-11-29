import sympy as sp

# Найти частные производные функции f(x, y) = tg(xy) / x^y
x, y = sp.symbols('x y')
f = sp.tan(x*y) / x**y
der_x= f.diff(x).simplify()
der_y = f.diff(y).simplify()
der_xx = f.diff(x, 2).simplify()
der_yy = f.diff(y, 2).simplify()
der_xy = der_x.diff(y).simplify()
der_yx = der_y.diff(x).simplify()

# Вывод результатов

print(f'Частные производные функции f(x, y) = tg(xy) / x^y:')

print(f'df/dx = {der_x}')

print(f'df/dy = {der_y}')

print(f'd^2f/dx^2 = {der_xx}')

print(f'd^2f/dy^2 = {der_yy}')

print(f'\nЧастные производные df/dy и df/dx:')

print(f'df/dy = {der_xy}')

print(f'df/dx = {der_yx}')