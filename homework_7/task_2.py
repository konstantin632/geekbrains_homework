#2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
#Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
#Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import  ABC,abstractmethod

class Clothes(ABC):

    @abstractmethod
    def expense(self):
        "вычисление стоимости одежды"

    @abstractmethod
    def __add__(self, other):
        "cложение стоимости одежды"

class Coat(Clothes) :

    def __init__(self,title,size):
        self.title=title
        self.size=size

    @property
    def expense(self):
        if self.title=='пальто':
            self.result=self.size/6.5+0.5
            return f'расход ткани на данное пальто - {self.result}'
        else:
           return 'это не пальто'

    def __add__(self, other):
        return self.result+other.result

class Costume(Clothes) :

    def __init__(self,title,size):
        self.title=title
        self.size=size

    @property
    def expense(self):
        if self.title=='костюм':
           self.result = 2*self.size+0.3
           return f'расход ткани на данный костюм - {self.result}'
        else:
            return 'это не костюм'

    def __add__(self, other):
        return self.result+other.result

my_costume=Costume('костюм',5)
my_coat=Coat('пальто',4)
my_coat2=Coat('пальто',4)

print(my_coat.expense)
print(my_costume.expense)
print(my_coat2.expense)

print(my_coat+my_costume)
