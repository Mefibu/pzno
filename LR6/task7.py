import numpy as np
from scipy.linalg import norm

# Заданная матрица
A = np.array([
    [12, -1, 3],
    [1, 10, 0],
    [-7, 2, 3]
])

# 1. Встроенная функция для спектральной нормы
spectral_norm_builtin = norm(A, ord=2)

# 2. Спектральная норма по определению (максимальная сингулярная величина)
u, s, vt = np.linalg.svd(A)  # Сингулярное разложение
spectral_norm_definition = max(s)

# Вывод результатов
print("Spectral norm (built-in):", spectral_norm_builtin)
print("Spectral norm (definition):", spectral_norm_definition)
