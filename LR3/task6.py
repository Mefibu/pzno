import numpy as np
import matplotlib.pyplot as plt

# Интервал значений для x и y
x = np.linspace(-3, 3, 400)
y = np.linspace(-3, 3, 400)

# Создаем сетку координат
X, Y = np.meshgrid(x, y)

# Неявная функция
Z = (X**2 + Y**2)**2 - 7 * (X**2 - Y**2)

# Построение контура при Z = 0
plt.figure(figsize=(8, 8))
plt.contour(X, Y, Z, levels=[0], colors='violet')

# Настройки графика
plt.title(r'График неявной функции $(x^2 + y^2)^2 - 7(x^2 - y^2) = 0$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

# Показать график
plt.show()
