#2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.
with open('task_2.txt','r') as file:
    list_string=file.readlines()
    for i in range(len(list_string)):
        sub_string = list_string[i].split()
        print(f'{i+1} string has {len(sub_string)} words')

