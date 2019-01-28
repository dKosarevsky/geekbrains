# class Car:
#
#     def __init__(self, model, color, year):
#         self.modules = []
#         self.model = model
#         self.color = color
#         self.year = year
#
#     @staticmethod
#     def beep():
#         print('BEEEEP!')
#
#     def __add__(self, other):
#         self.modules.append(other)
#         return self
#
#     def __str__(self):
#         return 'Автомобиль модели {}, цвета {}, год выпуска {}'.format(self.model, self.color, self.year)
#
#     # def __repr__(self):
#     #     return 'Только для внутренних нужд!'
# Car.beep()
#
# car = Car('lada', 'black', 1990)
# module = 'Кондиционер'
# car = car + module
# print(car)


class my_dict(dict):

    def __setitem__(self, key, value):
        print(key, value)
        return super().__setitem__(key, value)

    def __getitem__(self, item):
        if item == 'secret':
            return '*** secret ***'
        else:
            return super().__getitem__(item)

x = my_dict()
x['name'] = 'Ivan'
x['secret'] = 'qwerty'
print(x)
print(x['secret'])

