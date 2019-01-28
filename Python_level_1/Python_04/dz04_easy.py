# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

import random

list = [random.randint(0, 10) for _ in range(8)]
print(list)

list2 = [i ** 2 for i in list]
print(list2)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

print()
fruits1 = ['apple', 'banana', 'watermelon', 'orange', 'lemon', 'kivi', 'mandarin']
fruits2 = ['apple', 'lemon', 'melon', 'orange', 'lime', 'pear', 'pomelo', 'grapefruit']

fruits3 = [i for i in fruits1 if i in fruits2]
print(fruits3)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

print()
lst = [random.randint(-100, 100) for _ in range(28)]
print(lst)

lst2 = [i for i in lst if i % 3 == 0 and i > 0 and i % 4 != 0]
print(lst2)