#1. Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
#Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
#Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.

class Matrix:
    def __init__(self,list_of_lists):
        self.list_of_lists=list_of_lists
    def __str__(self):
        return f'{self.list_of_lists}'
    def __add__(self,other):
        sum_matrix=[[]]
        if len(self.list_of_lists)==len(other.list_of_lists) and len(self.list_of_lists[0])==len(other.list_of_lists[0]):
           result = [[self.list_of_lists[i][j] + other.list_of_lists[i][j] for j in range (len(self.list_of_lists[0]))]
                     for i in range(len(self.list_of_lists))]
           return result
        else:
            return f'у матриц различные размерности'

my_matrix=Matrix([[0,0,1,1],[0,0,0,0]])
my_matrix1=Matrix([[1,1,1,0],[1,1,1,0]])
print(my_matrix+my_matrix1)
