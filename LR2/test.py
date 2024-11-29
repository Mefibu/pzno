import numpy as np
def replace_positive_with_negative_sum(input_file='LR2/input.csv', output_file='LR2/output.csv'):
    # Читаем вектор из файла
    vector = np.loadtxt(input_file, delimiter=',')  # Считываем вектор из CSV файла
    
    # Вычисляем сумму отрицательных элементов
    negative_sum = np.sum(vector[vector < 0])
    
    # Заменяем положительные элементы на сумму отрицательных
    vector[vector > 0] = negative_sum
    
    # Записываем результирующий вектор в файл
    np.savetxt(output_file, vector, delimiter=',', fmt='%f')

# Вызов функции
replace_positive_with_negative_sum()

