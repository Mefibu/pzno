import numpy as np
import matplotlib.pyplot as plt

# Определение функции z(x, y)
def z_func(x, y):
    return np.sin(x - 2 * y)**2 * np.exp(-np.abs(y))

# Интервалы для x и y
x = np.linspace(0, np.pi, 100)
y = np.linspace(-1, 1, 100)
X, Y = np.meshgrid(x, y)
Z = z_func(X, Y)

# --- Каркасная поверхность (wire-frame) ---
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(1, 1, 1, projection='3d')

# Построение каркасной поверхности
ax.plot_wireframe(X, Y, Z, rstride=5, cstride=5)
ax.set_title('Каркасная поверхность (wire-frame)')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()

# --- Поверхность с линиями уровня (surface) ---
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(1, 1, 1, projection='3d')

# Построение поверхности
surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
ax.set_title('Поверхность с линиями уровня (surface)')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# Добавляем цветовую полосу
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)

plt.show()

# --- Поверхность с несколькими точками обзора ---
fig = plt.figure(figsize=(12, 8))

ax1 = fig.add_subplot(221, projection='3d')
ax1.plot_surface(X, Y, Z, cmap='coolwarm', edgecolor='none')
ax1.view_init(30, 45)
ax1.set_title('Вид под углом 30°/45°')

ax2 = fig.add_subplot(222, projection='3d')
ax2.plot_surface(X, Y, Z, cmap='coolwarm', edgecolor='none')
ax2.view_init(60, 60)
ax2.set_title('Вид под углом 60°/60°')

ax3 = fig.add_subplot(223, projection='3d')
ax3.plot_surface(X, Y, Z, cmap='coolwarm', edgecolor='none')
ax3.view_init(90, 90)
ax3.set_title('Вид под углом 90°/90°')

ax4 = fig.add_subplot(224, projection='3d')
ax4.plot_surface(X, Y, Z, cmap='coolwarm', edgecolor='none')
ax4.view_init(120, 30)
ax4.set_title('Вид под углом 120°/30°')

plt.tight_layout()
plt.show()
