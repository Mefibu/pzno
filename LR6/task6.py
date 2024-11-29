import numpy as np
from scipy.linalg import lstsq, pinv, qr, svd

# Матрица и вектор
A = np.array([[-1, 6], [2, 7], [-1, 5]])
b = np.array([1, 1, 1])

# 1. Метод наименьших квадратов (lstsq)
x1, _, _, _ = lstsq(A, b)

# 2. Использование псевдообратной матрицы (pinv)
x2 = pinv(A).dot(b)

# 3. Разложение QR
Q, R = qr(A, mode='economic')
x3 = np.linalg.inv(R).dot(Q.T).dot(b)

# 4. Сингулярное разложение (SVD)
U, s, VT = svd(A, full_matrices=False)
S_inv = np.diag(1 / s)
x4 = VT.T @ S_inv @ U.T @ b

# Вывод результатов
print("Pseudo-solution (lstsq):", x1)
print("Pseudo-solution (pinv):", x2)
print("Pseudo-solution (QR):", x3)
print("Pseudo-solution (SVD):", x4)
