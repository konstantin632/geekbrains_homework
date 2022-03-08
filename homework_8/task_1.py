#1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self,string_data):
        self.string_data=string_data

    @classmethod
    def get_int_data(cls,string_data):
        dict={1:'день',2:'месяц',3:'год'}
        data_list=string_data.split('-')
        for i in range(len(data_list)):
            if data_list[i][0] == '0':
                data_list[i] = data_list[i][1::]
            result_data=list(map(int,data_list))
        return result_data
    @staticmethod
    def validation(string_data):
        data_list = string_data.split('-')
        for i in range(len(data_list)):
          if data_list[i][0]=='0':
              data_list[i]=data_list[i][1::]
        if int(data_list[0])>31 or int(data_list[0])<1:
            return False
        elif int(data_list[1])>12 or int(data_list[1])<1:
            return False
        return True

my_data=Data('02-03-2014')
print(my_data.string_data)

print(Data.get_int_data('02-03-2014'))

print(Data.validation('31-13-2043'))
