#6. Если фирма отработала с прибылью, вычислите рентабельность выручки.
# Это отношение прибыли к выручке.
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.

gain=float(input('Какова выручка фирмы?'))

expenses=float(input('Каковы расходы фирмы?'))

if gain>expenses:
    print('Фирма приносит прибыль!')
    profit=gain-expenses
    profitability=profit/gain

    print(f'Рентабельность выручик:{profitability:.3f}')

    number_of_staff=int(input('Введите число сотрудников фирмы:'))
    print(f'Прибыль в расчёте на одного сотрудника:{profit/number_of_staff:.3f}')

elif gain<expenses:
    print('Фирма работает в убыток!')

else:
    print('Фирма работает в "0"')