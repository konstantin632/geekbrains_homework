#7. Создать вручную и заполнить несколькими строками текстовый файл,
#в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
#Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
#Если фирма получила убытки, в расчёт средней прибыли её не включать.
#Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
#Итоговый список сохранить в виде json-объекта в соответствующий файл.

import json

dict_firms={}
dict_average={}
average_sum=0
count=0

with open('task_7.txt','r',encoding='utf-8') as file:
  with open('task_7.json','w',encoding='utf-8') as file1:
     intput_list=file.readlines()
     for i in range(len(intput_list)):
         sub_list=intput_list[i].split()
         dict_firms[sub_list[0]]=float(sub_list[2])-float(sub_list[3])
         if dict_firms[sub_list[0]]>0:
            count+=1
            average_sum+=dict_firms[sub_list[0]]
     dict_average['average_profit']=average_sum/count
     json.dump([dict_firms,dict_average],file1)



