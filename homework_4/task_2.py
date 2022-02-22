#2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.


input_list=input('Введите через пробел элементы списка:').split()
input_list_int=[int(item) for item in input_list]

new_list=[input_list_int[i] for i in range(1,len(input_list_int)) if  input_list_int[i]>input_list_int[i-1] ]
print(new_list)

