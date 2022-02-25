#6. Сформировать (не программно) текстовый файл.
# В нём каждая строка должна описывать учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету.
# Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета были все типы занятий.
#Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
def filter_of_numbers(string=str):
    out_string=''
    for i in range(len(string)):
        if string[i] not in '1234567890':
            break
        out_string+=string[i]
    if out_string=='':
        return 0
    return float(out_string)

dict={}

with open('task_6.txt','r',encoding='utf-8') as file:
    input_list=file.readlines()
    for i in range(len(input_list)):
        sum_hours=0
        sub_string=input_list[i].split()
        for j in range(1,4):
            sum_hours+=filter_of_numbers(sub_string[j])
        dict[sub_string[0][:-1]]=sum_hours

print(dict)
