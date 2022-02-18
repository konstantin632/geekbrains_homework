#4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции возведения числа в степень.

def my_func(x=float,y=int):
    return x**y
x=float(input('Введите число:'))
y=int(input('Введите степень:'))
print(my_func(x,y))

def my_func_2(x=float,y=int):
    if y<0:
      result=1
      for i in range(abs(y)):
          result*=1/x
      return result
    else:
        return 'rate should be negative'

print(my_func_2(x,y))
