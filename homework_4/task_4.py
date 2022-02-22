#4. Представлен список чисел. Определите элементы списка, не имеющие повторений.
# Сформируйте итоговый массив чисел, соответствующих требованию.
# Элементы выведите в порядке их следования в исходном списке.
# Для выполнения задания обязательно используйте генератор.

input_list=input('Введите через пробел элементы списка:').split()
input_list_int=[int(item) for item in input_list]

list_gen=[element for element in input_list_int if input_list_int.count(element)==1]

print(list_gen)