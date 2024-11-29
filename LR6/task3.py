import numpy as np
from scipy.misc import derivative
from scipy.integrate import quad

# Функция
f = lambda x: x**3 + x**2 + x

# Точка, в которой нужно найти производные
x0 = 1
dx = 1e-6

# Первая производная с использованием встроенной функции derivative
first_derivative_scipy = derivative(f, x0, dx=dx)

# Вторая производная с использованием встроенной функции derivative
second_derivative_scipy = derivative(f, x0, dx=dx, n=2)

# Первая производная (центральная разностная формула)
first_derivative_formula = (f(x0 + dx) - f(x0 - dx)) / (2 * dx)

# Вторая производная (центральная разностная формула)
second_derivative_formula = (f(x0 + dx) - 2 * f(x0) + f(x0 - dx)) / (dx**2)

# Интегрирование функции f от 0 до x0 (в данном случае от 0 до 1)
integral_result, _ = quad(f, 0, x0)

# Вывод результатов
print("First derivative (using scipy derivative):", first_derivative_scipy)
print("Second derivative (using scipy derivative):", second_derivative_scipy)
print("First derivative (using central difference formula):", first_derivative_formula)
print("Second derivative (using central difference formula):", second_derivative_formula)
print("Integral of f from 0 to 1:", integral_result)
