#5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы).
# Нужно получить результат вычисления произведения всех элементов списка.
from functools import reduce

orig_list=[i for i in range(100,1001) if i%2==0]

result=reduce(lambda x,y:x*y,orig_list)
print(f'composition={result}')
