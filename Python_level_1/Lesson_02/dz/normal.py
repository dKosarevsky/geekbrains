# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

import math

a = [2, -5, 8, 9, -25, 25, 4]
result = []

for val in a:
    if val >= 0:
        #Первый вариант
        root_num = math.sqrt(val)
        #Второй вариант
        root_num = val ** 0.5
        if root_num == int(root_num):
            result.append(int(root_num))
print(result)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)
months = ['', 'января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября',
          'декабря']
days = ['', 'первое', 'второе', 'третье', 'четвертое', 'пятое', 'шестое', 'седьмое', 'восьмое', 'девятое', 'десятое',
        'одиннадцатое', 'двенадцатое', 'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое', 'семнадцатое',
        'восемнадцатое', 'девятнадцатое', 'двадцатое', 'двадцать первое', 'двадцать второе', 'двадцать третье',
        'двадцать чертвертое', 'двадцать пятое', 'двадцать шестое', 'двадцать седьмое', 'двадцать восьмое',
        'двадцать девятое', 'тридцатое', 'тридцать первое']

date = '02.11.2013'
day, month, year = date.split('.')
day = int(day)
month = int(month)
year = int(year)
print(days[day], months[month], year, 'года.')

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
import random

rand_list = []
elem_count = int(input('Введите количество элементов:'))

i = 0
while i < elem_count:
    rand_list.append(random.randint(-100, 100))
    i += 1
print(rand_list)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]
a = [1, 2, 4, 5, 6, 2, 5, 2]

first_a = list(set(a))
print(first_a)

second_a = []
for elem in a:
    if a.count(elem) == 1:
        second_a.append(elem)

print(second_a)