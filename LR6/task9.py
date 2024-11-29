import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange, CubicSpline, interp1d


# Данные
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([-8, 3, 5, -1, 2, 0])

# 1. Интерполяционный многочлен Лагранжа
poly = lagrange(x, y)

# 2. Интерполяция кубическим сплайном
cs_cubic = CubicSpline(x, y)

# 3. Интерполяция линейным сплайном (замена на interp1d)
cs_linear = interp1d(x, y, kind='linear')

# Новые точки для интерполяции
x_new = np.linspace(0, 5, 100)
y_poly = poly(x_new)
y_cubic = cs_cubic(x_new)
y_linear = cs_linear(x_new)

# Графики
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'o', label='Data points', markersize=8)
plt.plot(x_new, y_poly, label='Lagrange Polynomial', linestyle='--')
plt.plot(x_new, y_cubic, label='Cubic Spline', linestyle='-')
plt.plot(x_new, y_linear, label='Linear Spline', linestyle=':')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Interpolation: Lagrange and Splines")
plt.legend()
plt.grid()
plt.show()
