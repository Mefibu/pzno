import numpy as np
def is_positive_definite(matrix):
    for k in range(1, matrix.shape[0] + 1):
        if np.linalg.det(matrix[:k, :k]) <= 0:
            return False
    return True

# Примеры матриц для проверки
matrix_A = np.array([
    [14, 6, 3],
    [4, 9, -4],
    [3, -4, 9]
])

matrix_B = np.array([
    [2, 8, -8, 43, -3],
    [3, 0, -1, 3, 0],
    [7, -2, -4, 6, 2],
    [7, -5, 1, -5, -3],
    [-2, -5, 7, 6, -3]
])

# Проверка матриц
is_A_positive_definite = is_positive_definite(matrix_A)
is_B_positive_definite = is_positive_definite(matrix_B)

print("Матрица А ", is_A_positive_definite)

print("Матриця B", is_B_positive_definite)