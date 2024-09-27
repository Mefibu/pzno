import random

def find_best_row(matrix, min_free_seats=1):
  """Находит ряд с максимальным количеством свободных мест подряд.

  Args:
    matrix: Матрица, представляющая рассадку на концерте.
    min_free_seats: Минимальное количество свободных мест подряд.

  Returns:
    Номер ряда с максимальным количеством свободных мест.
  """

  max_free_seats = 0
  max_free_row = -1

  for i in range(len(matrix)):
      current_free_seats = 0
      for j in range(len(matrix[0])):
          if matrix[i][j] == 0:
              current_free_seats += 1
          else:
              if current_free_seats >= min_free_seats and current_free_seats > max_free_seats:
                  max_free_seats = current_free_seats
                  max_free_row = i
              current_free_seats = 0

      # Проверяем последний ряд, если все места свободны
      if current_free_seats >= min_free_seats and current_free_seats > max_free_seats:
          max_free_seats = current_free_seats
          max_free_row = i

  return max_free_row + 1  # Номера рядов начинаются с 1
def generate_random_matrix(rows, cols, min_value, max_value):
  """Генерирует матрицу заданного размера, заполненную случайными числами в заданном диапазоне.

  Args:
    rows: Количество строк.
    cols: Количество столбцов.
    min_value: Минимальное значение.
    max_value: Максимальное значение.

  Returns:
    Сгенерированная матрица.
  """

  matrix = [[random.randint(min_value, max_value) for _ in range(cols)] for _ in range(rows)]
  return matrix

def print_matrix(matrix):
  """Выводит матрицу на экран в удобочитаемом формате."""
  for row in matrix:
    print(row)

# Задаем параметры матрицы
rows = 15
cols = 30
min_value = 0
max_value = 1  # Для матрицы с нулями и единицами

# Создаем матрицу
matrix = generate_random_matrix(rows, cols, min_value, max_value)

# Выводим матрицу на экран
print("Сгенерированная матрица:")
print_matrix(matrix)

best_row = find_best_row(matrix, min_free_seats=3)
print("Лучший ряд для компании:", best_row)