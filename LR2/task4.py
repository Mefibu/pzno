import numpy as np


points = np.random.randint(0, 11, (10, 2))


dist_matrix = np.zeros((10, 10))


for i in range(10):
    for j in range(10):
        dist_matrix[i, j] = np.max(np.abs(points[i] - points[j]))


closest_point_index = np.argmin(dist_matrix[0, 1:]) + 1

print("Точки:\n", points)
print("Матрица расстояний:\n", dist_matrix)
print("Ближайшая точка к первой точке:", points[closest_point_index])
