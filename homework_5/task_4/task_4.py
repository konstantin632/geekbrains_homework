#4. Создать (не программно) текстовый файл со следующим содержимым:
#One — 1
#Two — 2
#Three — 3
#Four — 4
#Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

dict={'One':'Один','Two':'Два','Three':'Три','Four':'Четыре'}
out_list=''
with open('task_4.txt','r', encoding='utf-8') as file:
 with open('task_4_out.txt','w', encoding='utf-8') as file_out:
    input_list=file.readlines()
    for i in range(len(input_list)):
        out_list = dict[input_list[i].split()[0]]
        for j in range(1,3):
           out_list+=' '+input_list[i].split()[j]
        file_out.write(out_list+'\n')