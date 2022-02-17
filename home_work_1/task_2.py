#2.Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

input_seconds=int(input())

hours=input_seconds//3600
input_seconds-=hours*3600
minutes=input_seconds//60
input_seconds-=minutes*60

print(f'{hours:02}:{minutes:02}:{input_seconds:02}')

