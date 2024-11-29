import numpy as np

# Создание блоков для матрицы A
# block1 = np.array([[6, 5, 4, 3, 2, 1], [-6, -5, -4, -3, -2, -1]])
block1 = np.arange(6,0,-1)
block2 = np.arange(-6,0,1)
block3 = np.full((2, 6), 2)
block4 = np.full((2, 6), 4)

# Соединение блоков в одну матрицу A
A = np.vstack([block1, block2, block3 ,block4])

# Вычисление куба каждого элемента
A_cubed = A ** 3

# Найти минимальное значение среди элементов матрицы
min_value = np.min(A_cubed)

print("Матрица A:\n", A)
print("\nМатрица A, возведённая в куб:\n", A_cubed)
print("\nМинимальное значение среди элементов куба матрицы:", min_value)
