from collections import Counter

file_content = open('roadside_picnic.txt', "r", encoding="utf-8")
text = file_content.read()

my_list = list(text)
result = dict(Counter(my_list))

for key, value in result.items():
  print(key, ':', value)
