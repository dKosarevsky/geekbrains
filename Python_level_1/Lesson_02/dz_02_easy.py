# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

print()
fruits = ['apple', 'banana', 'kivi', 'watermelon']

right_offset = len(max(fruits, key=len))

for index, item in enumerate(fruits, start=1):
    print('{}. {:>{}}'.format(index, item, right_offset))


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

print()
print()
fruits = ['apple', 'banana', 'pumpkin', 'kivi', 'watermelon', 'potato']
vegetables = ['potato', 'pumpkin', 'carrot', 'cabbage']
for word in vegetables:
    while word in fruits:
        fruits.remove(word)
print(fruits)
print (vegetables)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

print()
print()
new_numbers = []
numbers = [3, 10, 88, 145, 555, 888, 200, 4]
for number in numbers:
    if number % 2 == 0:
        new_numbers.append(number/4)
    else:
        new_numbers.append(number*2)
print(new_numbers)


