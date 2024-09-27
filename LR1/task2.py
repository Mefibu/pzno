import sys

sys.stdout.reconfigure(encoding='utf-8')

def is_prime(num):
  """Проверяет, является ли число простым"""
  if num <= 1:
    return False
  if num <= 3:
    return True
  if num % 2 == 0 or num % 3 == 0:
    return False
  i = 5
  while i * i <= num:
    if num % i == 0 or num % (i + 2) == 0:
      return False
    i += 6
  return True

def check_number(number):
  """Проверяет число по условию задачи"""
  number = str(number)  # Преобразуем число в строку для удобства обработки
  for i in range(len(number) - 1, -1, -1):
    if int(number[i]) % 2 != 0:
      new_number = int(number[:i+1])
      if is_prime(new_number):
        print(f"Число {new_number} - простое")
      else:
        print(f"Число {new_number} - составное")
      return
  print("В числе нет нечетных цифр")


phone_number = int(input("Введите номер телефона " ))
check_number(phone_number)
