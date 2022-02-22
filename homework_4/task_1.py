#1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.
from sys import argv
def salary(hours=float,pay=float,reward=float):
    return hours*pay+reward

print(f'salary={salary(float(argv[1]),float(argv[2]),float(argv[3]))}')
