#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.

def max_of_list(list):
    max=list[0]
    for el in list:
        if el>max:
            max=el
    return max

def max_sum(num_1,num_2,mum_3):
    list=[num_1,num_2,num_3]
    max_1=max_of_list(list)
    list.remove(max_1)
    max_2=max_of_list(list)
    return max_1+max_2

num_1=float(input('Введите первое число:'))
num_2=float(input('Введите второе число:'))
num_3=float(input('Введите третье число:'))

print(max_sum(num_1,num_2,num_3))
