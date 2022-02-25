#3. Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
sum_salary=0

with open('task_3.txt','r', encoding='utf-8') as file:
    list_string=file.readlines()
    for i in range(len(list_string)):
        data_list=list_string[i].split()
        sum_salary+=float(data_list[1])
        if float(data_list[1])<20000:
            print(f'{data_list[0]} has salary less than 20.000 ')
    print(f'average salary is {sum_salary/len(list_string)}')