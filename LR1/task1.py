import sys

sys.stdout.reconfigure(encoding='utf-8')

def calculate_e(epsilon):
  x = 1
  e = 0
  while True:
    new_e = (1 + x) ** (1 / x)
    if abs(new_e - e) < epsilon:
      return new_e
    e = new_e
    x /= 2

# Пример использования
epsilon = float(input("epsilon = " ))
result = calculate_e(epsilon)
print("Приближенное значение e с точностью", epsilon, "равно:", result)