#4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки нужно пронумеровать. Если слово длинное, выводить только первые 10 букв в слове.


sentence=input()

list_of_words=sentence.split()
i=1

for word in list_of_words:
   print(f'{word[:10]} соответствует {i} строке')
   i+=1