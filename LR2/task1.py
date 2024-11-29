# -*- coding: utf-8 -*-

import numpy as np


# Task 1
# Даны 10 случайных точек iM пространства 2ℝ с целочисленными координатами.
points = np.random.randint(-10, 11, (10, 2))

# a.  Найти точку, наиболее удалённую от начала координат.
distances = np.linalg.norm(points, axis=1)
farthest_point = points[np.argmax(distances)]

# b. Sort points by distance from origin
sorted_points = points[np.argsort(distances)]

# c. Define v2normalize function
def v2normalize(x):
    norm = np.linalg.norm(x)
    return x / norm if norm != 0 else x

# d. Normalize the vectors and filter
# normalized_vectors = np.array([v2normalize(p) for p in sorted_points])
norms = np.linalg.norm(sorted_points, axis=1, keepdims=True)
normalized_vectors = np.divide(sorted_points, norms, where=norms!=0)

positive_normalized_vectors = normalized_vectors[np.all(normalized_vectors > 0, axis=1)]

print("Точки:\n", points)
print(f"Наиболее удаленная точка: {farthest_point}")
print("Сортировка в порядке возростания длин векторов :\n", sorted_points)
print("Массив нормированных векторов:\n",normalized_vectors)
print("Массив векторов с положительными координатами:\n", positive_normalized_vectors)



