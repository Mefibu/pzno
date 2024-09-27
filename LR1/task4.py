def count_words_by_length(filename, min_length=4, max_length=10):
  with open(filename, 'r', encoding='utf-8') as file:
    text = file.read()

  words = text.split()
  total_words = len(words)

  short_words = [word for word in words if len(word) < min_length]
  long_words = [word for word in words if len(word) > max_length]

  return total_words, len(short_words), len(long_words)

# Пример использования:
filename = "LR1/text2.txt"  # Замените на имя вашего файла
min_length = 4  # Указываем минимальную длину слова
max_length = 10  # Указываем максимальную длину слова
total, short, long = count_words_by_length(filename, min_length, max_length)

# Расчет процентов
percent_short = (short / total) * 100
percent_long = (long / total) * 100

print(f"Общее количество слов: {total}")
print(f"Процент коротких слов ({min_length} символов и меньше): {percent_short:.2f}%")
print(f"Процент длинных слов ({max_length} символов и более): {percent_long:.2f}%")