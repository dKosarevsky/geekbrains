# person = {'name': 'Ivan', 'damage': 100, 'health': 100}
# person2 = {'name': 'Ivan', 'damage': 100, 'health': 100, 'armor': 2}
#
# def attack(who_attack, who_defend):
#     pass
#
# def attack_with_armor(who_attack, who_defend):
#     pass


# class Car:
#
#     def __init__(self, car_model, car_color, cars):
#         self.model = car_model
#         self.color = car_color
#         cars.append(self)
#
#
# class Person:
#
#     def say(self, word):
#         print(word)
#
#     def go(self):
#         self.say('я иду')

# cars = []
# my_car = Car('Lada', 'Белая', cars)
# my_car2 = Car('Lada', 'Черная', cars)
#
# for car in cars:
#     print(car.model, car.color)
#     print(dir(car))

# print(my_car.model, my_car.color)
# my_car.color = 'Черная'
# print(my_car.model, my_car.color)
#
# my_person = Person()
# my_person.say('Hello!')

# class Car:
#
#     def __init__(self, car_model, car_color):
#         self._model = car_model
#         self.color = car_color
#
#     def get_model(self):
#         return self._model
#
#     def _secret(self):
#         print('secret method')
#
# my_car = Car('Lada', 'Черная')
# print(my_car.get_model())
# my_car._secret()
# my_car._model = 'Ferrari'
# print(my_car.get_model())

class Entity:

    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
        self.level = 1
        self.experience = 0
        self.next_level_exp = 100

    def add_experience(self, count):
        self.experience += count
        if self.experience >= self.next_level_exp:
            self._increase_level()
            self.next_level_exp *= 2

    def _increase_level(self):
        self.level += 1


class Person(Entity):

    def go(self):
        print('Идем вперед')


class Enemy(Entity):

    def __init__(self, name, health, damage, lvl):
        super().__init__(name, health, damage)
        self.level = lvl

# my_person = Person('Игрок', 100, 10)


# class Animal:
#
#     def __init__(self, name):
#         self.name = name
#
#     def run(self):
#         print('Убегаю!')
#
#
# class Rabbit(Animal):
#
#     def run(self):
#         print('Упрыгиваю..')
#
#
# class Bear(Animal):
#
#     def run(self):
#         print('Рычу и убегаю...')
#
#
# def make_fire(animals):
#     for animal in animals:
#         animal.run()
#
# my_animals_list = (Bear('Бурый медведь'), Rabbit('Белый кролик'))
# make_fire(my_animals_list)


# class Car:
#
#     def __init__(self, car_model, car_color):
#         self._model = car_model
#         self.color = car_color
#         self._secret = 'qwerty'
#
#     def get_model(self):
#         return self._model
#
#     def set_model(self, new_model, secret):
#         if secret == self._secret:
#             self._model = new_model


# class Car:
#
#     def __init__(self, car_model, car_color):
#         self._model = car_model
#         self.color = car_color
#
#     @property
#     def model(self):
#         return self._model
#
#     @model.setter
#     def model(self, new_model):
#         print('Нельзя менять модель!')
#
# car = Car(1, 2)
# car2 = Car(1, 2)
# car3 = Car(1, 2)
#
# print(car.model, car2.model, car3.model)
# car.model = 'Ferrari'
