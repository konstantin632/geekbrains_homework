#6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами, то есть характеристиками товара: название, цена, количество, единица измерения.
# Структуру нужно сформировать программно, запросив все данные у пользователя.

number=int(input('Введите число товаров:'))
list_of_items=[]

my_dic={}

for i in range(number):
    my_dic['название'] = input('введите название:')
    my_dic['цена']=float(input('введите цену:'))
    my_dic['количество']=float(input('количество:'))
    my_dic['ед'] = input('ед.:')
    my_tuple=(i,my_dic)
    list_of_items.append(my_tuple)

output_dic={}

for key in my_dic.keys():
    output_list=[]
    for i in range(number):
        el=list_of_items[i][1][key]
        output_list.append(el)
    output_dic[key] = output_list
print(output_dic)
