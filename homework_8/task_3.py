#3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо только числами.
# Класс-исключение должен контролировать типы данных элементов списка.

class Exception(Exception):
    def __init__(self,text):
        self.text=text
    @classmethod
    def check(cls,number):
        for x in number:
          if x not in '1234567890.':
            return False
        return True

out_list=[]
while True:
    el=input('enter number for list:')
    if el=='stop':
        break
    if Exception.check(el):
       out_list.append(float(el))
    else:
        raise Exception('Error:entered symbol is not a digit!')
print(out_list)
