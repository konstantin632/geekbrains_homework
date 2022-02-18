#5. Программа запрашивает у пользователя строку чисел, разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделённых пробелом и снова нажать Enter.
# Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
#Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def search_of_sign(input_string,sign):
    for el in input_string:
        if el==sign:
            return False
    return True

def sum_of_numbers(input_string):
    list_of_nums=input_string.split()
    flag=True
    sum=0
    for i in range(len(list_of_nums)):
        if search_of_sign(list_of_nums[i],'#'):
            sum+=int(list_of_nums[i])
        else:
            flag=False
            break
    return [sum,flag]

total_sum=0
input_string=input('Введите строку чисел, разделенных пробелом:')
total_sum+=sum_of_numbers(input_string)[0]
print(total_sum)

while sum_of_numbers(input_string)[1]!=False:
   input_string=input('Введите строку чисел, разделенных пробелом:')
   total_sum+=sum_of_numbers(input_string)[0]
   print(total_sum)
