#7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.
import cmath

class Complex_number:

    def __init__(self,real,image):
        self.real=real
        self.image=image

    def __str__(self):
        return f'{self.real}+j*{self.image}'

    def __add__(self, other):
        sum_complex=Complex_number(0,0)
        sum_complex.real=self.real+other.real
        sum_complex.image=self.image+other.image
        return sum_complex

    def __mul__(self, other):
        mul_complex = Complex_number(0, 0)
        mul_complex.real = self.real*other.real - self.image*other.image
        mul_complex.image = self.real*other.image + self.image*other.real
        return mul_complex

complex1=Complex_number(12,3)
complex2=Complex_number(13,4)

print(complex1)

print(complex2+complex1)

print(complex2*complex1)

print(complex(12,3)*complex(13,4))
