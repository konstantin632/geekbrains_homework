#1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.



with open('task_1.txt','w') as file:
    input_string = input('Введите данные в файл:')
    print(input_string,file=file)
    while input_string!='':
      input_string=input('Введите данные в файл:')
      print(input_string, file=file)

