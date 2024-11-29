
import numpy as np

# Определение функции для выполнения задачи 5
def replace_top_left_with_sum(input_file, output_file):
    """
    Функция считывает матрицу из файла input_file,
    заменяет элемент [0, 0] суммой всех элементов матрицы,
    и сохраняет изменённую матрицу в файл output_file.
    """
    # Чтение матрицы из файла
    matrix = np.loadtxt(input_file, delimiter=';')
    
    # Вычисление суммы всех элементов матрицы
    total_sum = np.sum(matrix)
    
    # Замена элемента [0, 0] на сумму
    matrix[0, 0] = total_sum
    
    # Запись изменённой матрицы в выходной файл
    np.savetxt(output_file, matrix, delimiter=';', fmt='%d')

# Создание примера input.csv с произвольной матрицей для демонстрации
input_matrix = np.random.randint(1, 10, (5, 5))
np.savetxt('LR2/input.csv', input_matrix, delimiter=';', fmt='%d')

# Применение функции к файлу input.csv и запись результата в output.csv
replace_top_left_with_sum('LR2/input.csv', 'LR2/output.csv')
