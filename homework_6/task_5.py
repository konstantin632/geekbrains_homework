#5. Реализовать класс Stationery (канцелярская принадлежность).
#определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
#создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
#в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
#создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self,title):
        self.title=title
    def draw(self):
        return 'Запуск отрисовки'

class Pen(Stationery):
    def draw(self):
        return 'Выбрана ручка'

class Pencil(Stationery):
    def draw(self):
        return 'Выбран карандаш'

class Handle(Stationery):
    def draw(self):
        return 'Выбран маркер'

my_stationary=Stationery('отрисовка')
print(my_stationary.draw())

my_pen=Pen('отрисовка ручкой')
print(my_pen.title)
print(my_pen.draw())

my_pencil=Pencil('отрисовка карандашом')
print(my_pencil.title)
print(my_pencil.draw())

my_handle=Handle('отрисовка маркером')
print(my_handle.title)
print(my_handle.draw())



