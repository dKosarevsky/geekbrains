# a = [1, 2, 3]
# b = a
#
# def test(some_list):
#     some_list.append(100)
#
#
# print(a)
# test(a)
# print(a)
# print(b)

# import copy
#
# a = [1, 2, 3, [0]]
# b = copy.deepcopy(a)
#
# b[3].append(100)
# print(a)
# print(b)

# a = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# print(a)
#
# for line in a:
#     for elem in line:
#         print(elem)

# name = input('Введите имя:')
# # print(name or 'Гость')
# print(name if name == 'admin' else 'Гость')

# a = 1
# b = 1
# print(a is b)
# a = 2
# print(a is b)


# def test(x):
#     if x > 0:
#         return 100
#
# result = test(-1)
# print(result is None)


# import random
#
# my_list = []
# for _ in range(10):
#     my_list.append(random.randint(-10, 10))
#
# print(my_list)
#
# my_list2 = [random.randint(-10, 10) for _ in range(10)]
# print(my_list2)
# my_list3 = [i for i in range(10) if i % 2 == 0]
# print(my_list3)
#
# some_int_list = [1, 2, 3, 4, 5, 6]
# some_str_result = [str(i) for i in some_int_list]
# print(some_str_result)
#
# my_dict = {i: i ** 2 for i in range(10)}
# print(my_dict)
#
# names = ['Ivan', 'Olga', 'Semen']
# salary = [100, 200, 300]
# my_dict = {key: value for key, value in zip(names, salary)}
# print(my_dict)

import re

str = 'Hello world!'
print(re.search('^[a-zA-Z]+', str))
print(re.match('[a-zA-Z]+', str))
print(re.findall('^[a-zA-Z]+', str))

print(r'Hello\n\t\r world ' + 'asd')

# a = [1, 2, 3]
#
# try:
#     print('Открываем соединение с сервером...')
#     f = open('111111')
# except FileNotFoundError as e:
#     print(e.args, e.filename, e.strerror)
#     print('Файл не найден')
# else:
#     print('Отправляем данные из файла на сервер...')
# finally:
#     print('Возврат ресурсов системе')

