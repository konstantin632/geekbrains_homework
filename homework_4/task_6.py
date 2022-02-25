#6. Реализовать два небольших скрипта:
#итератор, генерирующий целые числа, начиная с указанного;
#итератор, повторяющий элементы некоторого списка, определённого заранее.
from itertools import count,cycle

def generator_1(start=int,stop=int):
    output_list=[]
    for i in count(start):
        if i >stop:
            break
        output_list.append(i)
    return output_list

def generator_2(input_list=list,stop=int):
    output_list=[]
    for num,element in enumerate(cycle(input_list)):
        if num+1>stop:
            break
        output_list.append(element)
    return output_list

start=int(input('Enter start for gen_1:'))
stop=int(input('Enter stop for gen_1:'))

print(generator_1(start,stop))

input_list=input('Enter elements of your list for gen_2:').split()
stop=int(input('Enter stop of gen_2:'))

print(list(map(int,generator_2(input_list,stop))))
