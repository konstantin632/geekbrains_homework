#2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

def data_fun(name, surname, year_of_birth, city, email, telephone):
    return f'Имя пользователя:{name}, фамилия пользователя:{surname}, год рождения:{year_of_birth}, город:{city}, email:{email}, телефон' \
           f':{telephone}.'

new_list_data=[]
list_data=['name','surname','year_of_bearth','city','email','telephone']
for info in list_data:
    if info!='year_of_bearth':
       new_list_data.append(input(f'enter your {info}'))
    else:
        new_list_data.append(int(input(f'enter your {info}')))

print(data_fun(*new_list_data))
