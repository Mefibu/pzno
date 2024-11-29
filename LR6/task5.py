import numpy as np
from scipy.linalg import solve, inv, lstsq

# Матрица и вектор
A = np.array([[3, 2, -1], [2, -2, 4], [-1, 0.5, -1]])
b = np.array([1, -2, 0])

# 1. Прямое решение
x1 = solve(A, b)

# 2. Использование обратной матрицы
x2 = inv(A).dot(b)

# 3. Метод наименьших квадратов
x3, _, _, _ = lstsq(A, b)

print("Solution (solve):", x1)
print("Solution (inverse):", x2)
print("Solution (lstsq):", x3)
