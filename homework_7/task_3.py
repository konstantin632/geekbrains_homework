#3. Реализовать программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
# соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
# вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение,
# уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
#В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
#Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.

class Cell:

    def __init__(self,number_of_cells):
        self.number_of_cells=number_of_cells

    def __add__(self,other):
        sum_cells=self.number_of_cells + other.number_of_cells
        return Cell(sum_cells)

    def __sub__(self, other):
        if self.number_of_cells!=other.number_of_cells:
            sum_cells = self.number_of_cells - other.number_of_cells
            return Cell(sum_cells)

    def __mul__(self, other):
        sum_cells = self.number_of_cells * other.number_of_cells
        return Cell(sum_cells)

    def __truediv__(self, other):
        sum_cells = self.number_of_cells // other.number_of_cells
        return Cell(sum_cells)

    def make_order(self,number_in_line):
        number_of_lines=self.number_of_cells // number_in_line + int(bool(self.number_of_cells % number_in_line))
        out_str=''
        for i in range(number_of_lines):
            if i==number_of_lines-1 and  bool(self.number_of_cells % number_in_line):
                number_in_line=self.number_of_cells % number_in_line
            for j in range(number_in_line):
               out_str+='*'
            out_str+='\n'
        return out_str

my_cell=Cell(5)
my_cell1=Cell(3)
my_cell2=Cell(4)

print(my_cell.make_order(3))

print((my_cell+my_cell1+my_cell2).make_order(5))

print((my_cell*my_cell1).make_order(5))

print((my_cell/my_cell1).make_order(4))
