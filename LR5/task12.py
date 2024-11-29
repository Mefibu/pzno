import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Построить на одном рисунке 2 поверхности, заданные параметрически
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Первая поверхность
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x1 = np.outer(np.cos(u), np.sin(v))
y1 = np.outer(np.sin(u), np.sin(v))
z1 = np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_surface(x1, y1, z1, color='b', alpha=0.5)

# Вторая поверхность
x2 = np.outer(np.cos(u), np.sin(v))
y2 = np.outer(np.sin(u), np.sin(v))
z2 = np.outer(np.ones(np.size(u)), np.sin(v))
ax.plot_surface(x2, y2, z2, color='r', alpha=0.5)

plt.show()
