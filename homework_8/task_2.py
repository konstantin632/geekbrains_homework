#2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class Exception(Exception):
    def __init__(self,text):
        self.text=text


my_excepption=Exception('Error:Division by zero')

number1=float(input('enter 1 number:'))
number2=float(input('enter 2 number:'))

if number2!=0:
    print(number1/number2)
else:
    print(my_excepption.text)
