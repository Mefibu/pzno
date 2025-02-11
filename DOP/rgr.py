import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import dblquad

# Определение подынтегральной функции
def integrand(x, y):
    return 1 / (100 + np.cos(x)**2 + np.cos(y)**2)

# 1. Функция для вычисления двойного интеграла с использованием формулы трапеций
def trapezoidal_double_integral(func, x_range, y_range, num_points):
    x = np.linspace(x_range[0], x_range[1], num_points)
    y = np.linspace(y_range[0], y_range[1], num_points)
    dx = (x_range[1] - x_range[0]) / (num_points - 1)
    dy = (y_range[1] - y_range[0]) / (num_points - 1)
    
    integral = 0.0
    for i in range(num_points):
        for j in range(num_points):
            weight = 1.0
            if i == 0 or i == num_points - 1:
                weight *= 0.5
            if j == 0 or j == num_points - 1:
                weight *= 0.5
            integral += weight * func(x[i], y[j])
    
    integral *= dx * dy
    return integral

# 2. Функция для вычисления двойного интеграла с использованием повторной квадратурной формулы (dblquad из SciPy)
def quadrature_double_integral(func, x_range, y_range):
    result, error = dblquad(func, y_range[0], y_range[1], lambda y: x_range[0], lambda y: x_range[1])
    return result

# 3. Построение трёхмерного графика подынтегральной функции
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)
Z = integrand(X, Y)

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_title('3D график подынтегральной функции')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')
plt.show()

# 4. Сравнение результатов, полученных разными методами при различных количествах точек разбиения
x_range = (-10, 10)
y_range = (-10, 10)
num_points_list = [10, 20, 50, 100]

print("Сравнение методов вычисления двойного интеграла:\n")
for num_points in num_points_list:
    trapezoidal_result = trapezoidal_double_integral(integrand, x_range, y_range, num_points)
    quadrature_result = quadrature_double_integral(integrand, x_range, y_range)
    print(f"Количество точек: {num_points}")
    print(f"  Результат методом трапеций: {trapezoidal_result}")
    print(f"  Результат методом квадратур: {quadrature_result}")
    print(f"  Разница: {abs(trapezoidal_result - quadrature_result)}\n")

