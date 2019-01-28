# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

print()

class Car:

    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn_right(self):
        print('Машина повернула направо')

    def turn_left(self):
        print('Машина повернула налево')

class TownCar(Car):
    pass

class SportCar(Car):
    pass

class WorkCar(Car):
    pass

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police = False):
        super().__init__(speed, color, name, is_police)
        self.is_police = True
        print()
        print('Это полиция!')

car1 = TownCar('20 км/ч', 'Black', 'Ford_Focus')
print(car1.speed, car1.color, car1.name)
car1.turn_right()
print()

car2 = SportCar('220 км/ч', 'Red', 'Chevrolet_Corvette')
print(car2.speed, car2.color, car2.name)
car2.go()
print()

car3 = WorkCar('10 км/ч', 'Orange', 'Kamaz_Снегоуборщик')
print(car3.speed, car3.color, car3.name)
car3.turn_left()
print()

car4 = PoliceCar('0 км/ч', 'White-Blue', 'Lada_Xray')
print(car4.speed, car4.color, car4.name)
car4.stop()

car5 = PoliceCar('20 км/ч', 'White-Blue', 'UAZ_Patriot')
print(car5.speed, car5.color, car5.name)
car5.go()

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.