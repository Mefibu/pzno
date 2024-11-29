import numpy as np
import matplotlib.pyplot as plt

# Параметр t от 0 до 2π
t = np.linspace(0, 2 * np.pi, 1000)

# Параметрические функции x(t) и y(t)
x_t = 9 * np.sin(t / 10) - 0.5 * np.sin(t / 2) + (9 * t) / 10
y_t = 9 * np.cos(t / 10) + 0.5 * np.cos(t / 2) + (9 * t) / 10

# Построение графика
plt.figure(figsize=(8, 8))
plt.plot(x_t, y_t, label=r'$x(t), y(t)$', color='blue')

# Настройки графика
plt.title('Параметрически заданная функция')
plt.xlabel('x(t)')
plt.ylabel('y(t)')
plt.legend()
plt.grid(True)

# Показать график
plt.show()
