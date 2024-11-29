import numpy as np
import matplotlib.pyplot as plt

# Определение функций прямых
def y1(x):
    return 6*x - 2

def y2(x):
    return -x + 12

# Интервал для x
x = np.linspace(0, 5, 100)

# Координаты точки пересечения
x_intersect = 2
y_intersect = 10

# Построение графиков прямых
plt.figure(figsize=(8, 6))
plt.plot(x, y1(x), label=r'$y_1 = 6x - 2$', color='blue')
plt.plot(x, y2(x), label=r'$y_2 = -x + 12$', color='green')

# Отметим точку пересечения
plt.plot(x_intersect, y_intersect, 'ro')  # Точка пересечения
plt.text(x_intersect, y_intersect, f'({x_intersect}, {y_intersect})', fontsize=12, verticalalignment='bottom')

# Настройки графика
plt.title('Пересечение двух прямых')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)

# Показать график
plt.show()
