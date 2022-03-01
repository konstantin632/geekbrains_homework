#2. Реализовать класс Road (дорога).
#определить атрибуты: length (длина), width (ширина);
#значения атрибутов должны передаваться при создании экземпляра класса;
#атрибуты сделать защищёнными;
#определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
#использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
#проверить работу метода.

class Road:
    def __init__(self,length,width):
        self.__length = length
        self.__width = width

    def weight(self,density_of_road=20,thickness=10):
        self.__weight=density_of_road*thickness*self.__length*self.__width
        return f'the weight of road - {self.__length} sm*{self.__width} sm*{density_of_road} kg/sm^3*{thickness} sm = {self.__weight} kg'

my_road=Road(10*6,200)
print(my_road.weight())

