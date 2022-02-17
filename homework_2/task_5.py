#5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.

rating=[]
flag=True

N=int(input(('Введите первоначальное число рейтингов:')))

rating=[0]*N
for i in range(N):
    rating[i]=int(input())

flag=True
rating.reverse()

while flag:
    new_rating=input()
    if new_rating!='':
        new_rating=int(new_rating)
        if rating.count(new_rating)>0:
             rating.insert(rating.index(new_rating),new_rating)
        elif new_rating>rating[-1]:
             rating.append(new_rating)
        elif new_rating<rating[0]:
             rating.insert(0,new_rating)
    else:
        flag=False
rating.reverse()

for i in range(len(rating)):
  sep=','
  if i==len(rating)-1:
      sep='.'
  print(rating[i],end=f'{sep}')