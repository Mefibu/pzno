import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar

# Заданная функция
f = lambda x: (x - 3)**2 + (x + 5)**2

# 1. Метод Брента
res_brent = minimize_scalar(f, method='brent')

# 2. Метод золотого сечения
res_golden = minimize_scalar(f, method='golden')

# 3. Метод ограничений (bounded)
res_bounded = minimize_scalar(f, method='bounded', bounds=(-10, 10))

# Вывод результатов
print("Minimum (Brent):", res_brent.x)
print("Minimum (Golden Section):", res_golden.x)
print("Minimum (Bounded):", res_bounded.x)

# Построение графика функции
x = np.linspace(-10, 10, 500)
y = f(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label="f(x) = (x-3)^2 + (x+5)^2", lw=2)
plt.axvline(res_brent.x, color='r', linestyle='--', label=f"Min (Brent) x={res_brent.x:.2f}")
plt.axvline(res_golden.x, color='g', linestyle='--', label=f"Min (Golden) x={res_golden.x:.2f}")
plt.axvline(res_bounded.x, color='b', linestyle='--', label=f"Min (Bounded) x={res_bounded.x:.2f}")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Finding the Minimum of the Function")
plt.legend()
plt.grid()
plt.show()
