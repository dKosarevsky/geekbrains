# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.



# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный класс, который наследуется от базового - Игрушка


class Toy:

    def __init__(self, name, colour):
        self.name = name
        self.colour = colour


class ToyAnimal(Toy):

    def __init__(self, name, colour):
        Toy.__init__(self, name, colour)
        self.type = 'Зверята'


class ToyMult(Toy):

    def __init__(self, name, colour):
        Toy.__init__(self, name, colour)
        self.type = 'Мульперсонаж'


class ToyFactory:

    def create_toy(self, name, colour, type):
        self._buy_materials()
        self._making()
        self._set_colour()
        if type == 'Зверята':
            return ToyAnimal(name, colour)
        elif type == 'Мульперсонаж':
            return ToyMult(name, colour)

    def _buy_materials(self):
        print('Закупка материалов.')

    def _making(self):
        print('Изготовление игрушки.')

    def _set_colour(self):
        print('Покраска игрушки.')


factory = ToyFactory()
toy = factory.create_toy('Карл', 'красный', 'Зверята')

print()
print('Игрушка готова: ')
print(toy.name, toy.colour, toy.type)