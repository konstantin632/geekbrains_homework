#2. Для списка реализовать обмен значений соседних элементов. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
#При нечётном количестве элементов последний сохранить на своём месте. Для заполнения списка элементов нужно использовать функцию input().

flag=True
input_list=[]

while flag:
   input_list.append(input())
   if input_list[-1]=='':
        flag=False
my_list=input_list[:-1]

if len(my_list)%2==0:
    for i in range(0,len(my_list)-1,2):
       my_list[i],my_list[i+1]=my_list[i+1],my_list[i]
    print(my_list)
else:
    for i in range(0,len(my_list)-2,2):
       my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    print(my_list)