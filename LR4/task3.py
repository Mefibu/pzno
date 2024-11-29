import pandas as pd

# Загрузка данных из текстовых файлов
students1 = pd.read_csv('students1.txt', sep='\t')
students2 = pd.read_csv('students2.txt', sep='\t')

# Объединение данных из двух таблиц по общему столбцу 'Name'
students_data = pd.merge(students1, students2, on='Name', how='inner')

# Расчет коэффициентов корреляции между заданными предметами
correlation_prog1_prog2 = students_data['Програмування1'].corr(students_data['Програмування2'])
correlation_prog1_algorithms = students_data['Програмування1'].corr(students_data['Алгоритми і структури даних'])
correlation_prog2_algorithms = students_data['Програмування2'].corr(students_data['Алгоритми і структури даних'])

correlation_culture_analysis = students_data['Історія української культури'].corr(students_data['Функціональний аналіз'])

# Вывод коэффициентов корреляции
print(f'Коэффициент корреляции между Програмування1 и Програмування2: {correlation_prog1_prog2:.2f}')
print(f'Коэффициент корреляции между Програмування1 и Алгоритми і структури даних: {correlation_prog1_algorithms:.2f}')
print(f'Коэффициент корреляции между Програмування2 и Алгоритми і структури даних: {correlation_prog2_algorithms:.2f}')
print(f'Коэффициент корреляции между Історія української культури и Функціональний аналіз: {correlation_culture_analysis:.2f}')
