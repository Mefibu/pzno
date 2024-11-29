import numpy as np
import matplotlib.pyplot as plt

# Задаем параметры
a = 2  # Длина стороны квадрата
radius = a / 2  # Радиус вписанной окружности

# Создаем данные для окружности
theta = np.linspace(0, 2 * np.pi, 100)
x_circle = radius * np.cos(theta)
y_circle = radius * np.sin(theta)

# Создаем квадрат
square_x = [-radius, radius, radius, -radius, -radius]
square_y = [-radius, -radius, radius, radius, -radius]

# Построение графика
plt.figure(figsize=(6, 6))
plt.plot(x_circle, y_circle, label='Окружность', color='blue')
plt.plot(square_x, square_y, label='Квадрат', color='red')

# Выровнять масштабы осей
plt.gca().set_aspect('equal', adjustable='box')

# Настройки графика
plt.title('Окружность, вписанная в квадрат')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Сохранение изображения с dpi=400
plt.savefig('photo.png', dpi=400)

# Показать график
plt.show()
