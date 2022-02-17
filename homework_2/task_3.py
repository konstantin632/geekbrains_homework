#3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и dict.



month=int(input('Введите месяц:'))

# Решение через спики

list_of_monthes=[1,2,3,4,5,6,7,8,9,10,11,12]

index=list_of_monthes.index(month)

if index<=1 or index==11:
      print('It is winter')
elif list_of_monthes.index(month)<=4:
      print('It is spring')
elif list_of_monthes.index(month)<=7:
      print('It is summer')
else:
      print('It is autumn')

# Решение через словари


dict={1:'winter',2:'winter',
3:'spring',4:'spring',5:'spring',
6:'summer',7:'summer',
8:'summer',9:'autumn',10:'autumn',
11:'autumn',12:'winter'
}

for key,value in dict.items():
   if key==month:
      print(f'It is {value}')
      break