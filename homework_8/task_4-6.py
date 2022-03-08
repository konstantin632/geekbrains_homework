#4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите параметры,
# общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

#5. Продолжить работу над первым заданием.
# Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру (например, словарь).

#6. Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

class Exception(Exception):
    def __init__(self,text):
        self.text=text
    def __str__(self):
        return text

class Storehouse:

    def __init__(self):
        self.equipments={}

    def get_equipment(self,new_equipments):
        for key,value in new_equipments.items():
            if isinstance(value,str):
                raise Exception('Error:entered number of equipment should have digit type!')
            else:
              if key in self.equipments:
                 self.equipments[key]+=value
              else:
                 self.equipments[key]=value

    def get_equipment_from_firm(self,firm,new_equipment):
        if firm.give_equipment(new_equipment):
            equip_dict={new_equipment:1}
            self.get_equipment(equip_dict)

    def give_equipment_to_firm(self,firm,new_equipment):
        if new_equipment in self.equipments.keys() and self.equipments[new_equipment]>0:
            if firm.get_equipment(new_equipment):
                self.equipments[new_equipment]-=1

class Org_equipment:
    def __init__(self,country,price,equipments):
        self.country=country
        self.price=price
        self.equipments=[]

    def get_equipment(self,new_equipment):
        self.equipments.append(new_equipment)
        return True

    def give_equipment(self,new_equipment):
        if new_equipment in self.equipments:
           self.equipments.remove(new_equipment)
           return True
        else:
            return False


class Printer(Org_equipment):

    def get_equipment(self, new_equipment):
        if self.country == 'USA' and self.price<20000 and len(self.equipments)<12:
          self.equipments.append((new_equipment,self.country,self.price))
          return True

    def __str__(self):
        return f'list of printers of firm - {self.equipments}'

    def give_equipment(self,new_equipment):
        if (new_equipment,self.country,self.price) in self.equipments:
           self.equipments.remove((new_equipment,self.country,self.price))
           return True
        else:
            return False

class Skan(Org_equipment):
    def get_equipment(self, new_equipment):
        if self.country == 'Germany' and self.price < 15000 and len(self.equipments) < 12:
            self.equipments.append((new_equipment,self.country,self.price))
            return True

    def __str__(self):
        return f'list of skans of firm - {self.equipments}'

class Xerox(Org_equipment):
    def get_equipment(self, new_equipment):
        if self.country == 'Japan' and self.price < 25000 and len(self.equipments) < 2:
            self.equipments.append((new_equipment,self.country,self.price))
            return True

    def __str__(self):
        return f'list of xeroxes of firm - {self.equipments}'

store=Storehouse()
firm_of_printer=Printer('USA',15000,[])
firm_of_skan=Skan('Germany',13000,[])
firm_of_xerox=Xerox('Japan',15000,[])

store.get_equipment({'Printer XP':3,'Printer HP':2,'Xerox MN':2,'Skan TR':1})
print(store.equipments)

store.give_equipment_to_firm(firm=firm_of_printer,new_equipment='Printer XP')
print(firm_of_printer)
print(store.equipments)

store.give_equipment_to_firm(firm=firm_of_skan,new_equipment='Skan TR')
print(firm_of_skan)
print(store.equipments)

store.give_equipment_to_firm(firm=firm_of_skan,new_equipment='Skan TR')
print(firm_of_skan)
print(store.equipments)

store.give_equipment_to_firm(firm=firm_of_printer,new_equipment='Printer HP')
print(firm_of_printer)
print(store.equipments)

store.give_equipment_to_firm(firm=firm_of_printer,new_equipment='Printer HP')
print(firm_of_printer)
print(store.equipments)

store.get_equipment_from_firm(firm=firm_of_printer,new_equipment='Printer XP')
print(firm_of_printer)
print(store.equipments)
