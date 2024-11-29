import numpy as np
import matplotlib.pyplot as plt

# Определение константы e
e = np.exp(1)

# Интервалы
x1 = np.linspace(1, e, 100)  # Интервал для первой части ln(x)
x2 = np.linspace(e, 9, 100)  # Интервал для второй части x/e
x3 = np.linspace(9, 12, 100)  # Интервал для третьей части 9e^(8 - x)

# Определение кусочно-заданной функции
def f1(x):
    return np.log(x)

def f2(x):
    return x / e

def f3(x):
    return 9 * np.exp(8 - x)

# Построение графика
plt.figure(figsize=(8, 6))

# Первая часть: ln(x)
plt.plot(x1, f1(x1), label=r'$\ln(x), 1 \leq x \leq e$', color='blue', linestyle='-')

# Вторая часть: x/e
plt.plot(x2, f2(x2), label=r'$x/e, e < x \leq 9$', color='green', linestyle='--')

# Третья часть: 9e^(8 - x)
plt.plot(x3, f3(x3), label=r'$9e^{8 - x}, 9 < x \leq 12$', color='red', linestyle='-.')

# Настройки графика
plt.title('График кусочно-заданной функции')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)

# Показать график
plt.show()
