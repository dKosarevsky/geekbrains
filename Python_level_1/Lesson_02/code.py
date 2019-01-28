# print('Hello' + ' ' + 'world')
# print('Hello' ' ' 'world')
# print('Hello! ' * 3)
#
# url = 'http://yandex.ru'
# index = url.find('yandex')
# print(url.find('yandex'))
# print(url[index:])

# name = 'ivAn peTrov'

# print(name.title())
# print(name.upper())
# print(name.lower())
# print(len(name))

# name = 'Иван'
# surname = 'Петров'
# age = 30
# bank_account = 100.30
# print('Привет ' + name + ' ' + surname)
# print('Привет %s %s' % (name, surname))
# print('Привет {} {} {}'.format(name, surname, name))
# print('Привет {} {} вам на данный момент {} лет, на вашем банковском счету {} рублей'.format(name, surname, age, bank_account))

# my_list = [1, 2, 1]
# print(my_list)
# my_list[-1] = 100
# print(my_list[1:])
# print(my_list + [4, 5, 6])
# print(my_list)
# my_list.extend([4, 5, 6])
# print(my_list)
#
# my_list.remove(1)
# print(my_list)
#
# my_list.append(200)
# print(my_list)
# my_list.insert(2, 300)
# print(my_list)
#
# last_element = my_list.pop()
# print(last_element)
# my_list = [4, 5, 6, 7, 1, 2, 3, 3, 3, 3]
#
# print(my_list.count(3))
#
# my_list = ['zxcvzbnxcvznxc', 'aaaaaa', 'aa']
#
# my_list.sort(key=len)
# print(my_list)
#
# [1,2,3].reverse()

# my_list = ['Ivan', 'Andrey', 'Olga']
# if 'Ivan' in my_list:
#     print('Ivan есть в списке')
# a = [] # список
# b = () # кортеж
# c = {} # словарь

# my_tuple = (2, 3, 4)
# list(my_tuple).sort()

# fruits = ['apple', 'banana', 'mango', 'orange', 'melon']

# i = 0
# while i < len(fruits):
#     print(fruits[i])
#     i += 1

# for fruit in fruits:
#     print(fruit)
#     fruits.remove(fruit)

# for index, fruit in enumerate(fruits):
#     print(index, fruit)

# my_list = [1, 2, 3]
# name = 'Ivan'
# human = {'name': name, 'surname': 'Petrov', 'data': {}}
#
# my_list[0] = 100
# human['name'] = 'Vasya'
# print(my_list)
# print(human)
#
# my_list.append(200)
# human['age'] = None
# print(human)

# human = {'name': 'Ivan', 'surname': 'Petrov'}

# for key, value in human.items():
#     print(key, value)
#
# for key in human.keys():
#     print(key)

# for value in human.values():
#     print(value)

# print(human.pop('name'))
# print(human)
x = 3
y = 3
a = {1, 2, 3, x}
b = {y, 4, 5, 6}
# print(a)
# print(b)
# print(a == b)
# print(a >= b)
# print(a & b)
print(a - b)
# print(a | b)

words = ['Ivan', 'Oleg', 'Ivan', 'Olga', 'Oleg']
print(set(words))

a = {1, 2, 3}
b = set([1, 2, 3])
print(a, b)
