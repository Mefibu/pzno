import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Уравнение третьего порядка
def odes(t, y):
    y0, y1, y2 = y
    dy0 = y1
    dy1 = y2
    dy2 = -2 * y2 - y1 - 3  # Правая часть уравнения
    return [dy0, dy1, dy2]

# Начальные условия
y0 = -1  # y(0)
y1 = 2   # y'(0)
y2 = 3   # y''(0)

# Решение задачи на интервале [0, 10]
t_span = (0, 10)
initial_conditions = [y0, y1, y2]
solution = solve_ivp(odes, t_span, initial_conditions, t_eval=np.linspace(0, 10, 100))

# Извлекаем результаты
t = solution.t
y = solution.y[0]  # y(x)
y_prime = solution.y[1]  # y'(x)
y_double_prime = solution.y[2]  # y''(x)

# Построение графиков
plt.figure(figsize=(10, 6))
plt.plot(t, y, label="y(x)", lw=2)
plt.plot(t, y_prime, label="y'(x)", lw=2)
plt.plot(t, y_double_prime, label="y''(x)", lw=2)
plt.xlabel("x")
plt.ylabel("Functions")
plt.title("Solution to the Cauchy Problem")
plt.legend()
plt.grid()
plt.show()
