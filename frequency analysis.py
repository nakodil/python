from collections import Counter

# читаем текст из файла
source_file = open('roadside_picnic.txt', "r", encoding="utf-8")
text = source_file.read()

# создаем список
my_list = list(text)
# считаем повторы символов
result = dict(Counter(my_list))

# выводим результат на экран
# ключ : значение
for key, value in result.items():
  print(key, ':', value)

# пишем результат в файл
destination_file = open('result.txt', "w", encoding="utf-8")
destination_file.write(str(result))
