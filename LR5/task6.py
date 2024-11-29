
import sympy as sp

# Работа с функцией f(x, y) = x^2 + y^2
x, y = sp.symbols('x y')
f = x**2 + y**2
M = (1, 1)

# 1) Вычисление градиента функции f в точке M
grad_f = [sp.diff(f, var) for var in (x, y)]
grad_f_at_M = [grad.subs({x: M[0], y: M[1]}) for grad in grad_f]
print(f'Градиент функции в точке M: {grad_f_at_M}')

# 2) Производная функции в точке M по направлению вектора d = (2, -1)
d = (2, -1)
direction_derivative = sum([grad_f[i] * d[i] for i in range(2)])
direction_derivative_at_M = direction_derivative.subs({x: M[0], y: M[1]})
print(f'Производная функции в точке M по направлению d: {direction_derivative_at_M}')

# 3) Определение возрастания или убывания функции в точке M по направлению d
if direction_derivative_at_M > 0:
    print('Функция возрастает в точке M по направлению d')
elif direction_derivative_at_M < 0:
    print('Функция убывает в точке M по направлению d')
else:
    print('Функция не изменяется в точке M по направлению d')
