import numpy as np
import matplotlib.pyplot as plt

# Определим функции
def f(x):
    return x**3 + 2*x**2 + 1

def g(x):
    return (x - 1)**4

def u(x):
    return np.sqrt(x)

def v(x):
    return np.exp(-x**2)

# Интервалы
x1 = np.linspace(-1, 1, 100)  # Для f(x) и g(x)
x2 = np.linspace(0, 1, 100)   # Для u(x) и v(x)

# Построение всех графиков на одних осях
plt.figure(figsize=(10, 6))
plt.plot(x1, f(x1), label=r'$f(x) = x^3 + 2x^2 + 1$', color='b', linestyle='-', marker='o')
plt.plot(x1, g(x1), label=r'$g(x) = (x - 1)^4$', color='r', linestyle='--', marker='x')
plt.plot(x2, u(x2), label=r'$u(x) = \sqrt{x}$', color='g', linestyle='-.', marker='s')
plt.plot(x2, v(x2), label=r'$v(x) = e^{-x^2}$', color='m', linestyle=':', marker='d')
plt.title('Графики функций на одних осях')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

# Построение графиков на отдельных осях (две части)
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Графики для первой оси (f(x) и g(x))
axs[0, 0].plot(x1, f(x1), label=r'$f(x) = x^3 + 2x^2 + 1$', color='b', linestyle='-', marker='o')
axs[0, 0].plot(x1, g(x1), label=r'$g(x) = (x - 1)^4$', color='r', linestyle='--', marker='x')
axs[0, 0].set_title('Графики f(x) и g(x)')
axs[0, 0].set_xlabel('x')
axs[0, 0].set_ylabel('y')
axs[0, 0].legend()
axs[0, 0].grid(True)

# Графики для второй оси (u(x) и v(x))
axs[1, 0].plot(x2, u(x2), label=r'$u(x) = \sqrt{x}$', color='g', linestyle='-.', marker='s')
axs[1, 0].plot(x2, v(x2), label=r'$v(x) = e^{-x^2}$', color='m', linestyle=':', marker='d')
axs[1, 0].set_title('Графики u(x) и v(x)')
axs[1, 0].set_xlabel('x')
axs[1, 0].set_ylabel('y')
axs[1, 0].legend()
axs[1, 0].grid(True)

# Убираем пустые оси
axs[0, 1].axis('off')
axs[1, 1].axis('off')

plt.tight_layout()
plt.show()
