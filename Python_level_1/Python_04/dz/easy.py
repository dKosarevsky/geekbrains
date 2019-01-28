# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
source_list = [1, 2, 3, 4, 5, 6, 7, 8]
new_list = [i ** 2 for i in source_list]
print(new_list)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
fruits1 = ['banana', 'apple', 'grape', 'orange']
fruits2 = ['qiwi', 'apple', 'banana']

new_list = [i for i in fruits1 if i in fruits2]
print(new_list)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
import random

source_list = [random.randint(-10, 100) for _ in range(100)]
print(source_list)
new_list = [i for i in source_list if i % 3 == 0 and i >= 0 and i % 4 > 0]
print(new_list)