#4. Реализуйте базовый класс Car.
#у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
#опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
#добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
#для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат

class Car:
    def __init__(self,speed,color,name,is_police):
        self.speed=speed
        self.color=color
        self.name=name
        self.is_police=is_police
    def go(self):
        return 'машина поехала'
    def stop(self):
        return 'машина остановилась'
    def turn(self,direction):
        return f'машина повернула {direction}'
    def show_speed(self):
        return f'скорость не превышена - {self.speed}'

class Towncar(Car):
    def show_speed(self):
        if self.speed>60:
            return f'скорость превышена - {self.speed}>60'

class Workcar(Car):
    def show_speed(self):
        if self.speed>40:
            return f'скорость превышена - {self.speed}>40'

class Sportcar(Car):
    pass

class PoliceCar(Car):
    pass

police_car=PoliceCar(100,'black','BMW',True)

print(f'name of police car - {police_car.name}, police color -{police_car.color}, speed - {police_car.speed}')
print(police_car.go())
print(police_car.turn('налево'))

sport_car=Sportcar(300,'blue','Bentley',False)

print(f'name of police car - {sport_car.name}, police color - {sport_car.color}, speed - {sport_car.speed}')
print(sport_car.show_speed())

town_car=Towncar(70,'green','Mercedez',False)
print(f'name of police car - {town_car.name}, police color - {town_car.color}, speed - {town_car.speed}')
print(town_car.show_speed())
print(town_car.stop())
