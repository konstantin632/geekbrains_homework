#5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

sum=0
with open('task_5.txt','w') as file:
    file.write(input('введите набор чисел через пробелы:'))

with open('task_5.txt','r') as file:
    input_list=file.read().split()
    for i in range(len(input_list)):
        sum+=float(input_list[i])
print(f'Cумма чисел:{sum}')

