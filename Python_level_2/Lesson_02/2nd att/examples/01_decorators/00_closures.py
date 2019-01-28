
# -------------- Замыкания (closures ----------------------------------

# Замыкание - это функция, которая запоминает привязки свободных переменных 
# на момент определения функции, так что их можно использовать впоследствии при вызове функции, 
# когда область видимости, в которой она была определена, уже не существует.

# Реализуем функцию, вычисляющую среднее арифметическое значений, которые в неё передавались:

def make_averager():
    series = []
    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager

# При обращении к make_averager возвращается объект-функция averager. 
# При каждом вызове averager добавляет переданный аргумент в конец списка series
# и вычисляет текущее среднее значение:

print(' -- Демонстрация работы замыкания --')

avg = make_averager()
print(avg(10))
print(avg(11))
print(avg(12))


# Внутри функции averager переменная series является свободной переменной.
# Это означает, что переменная не связана в локальной области видимости.

# Python хранит имена локальных и свободных переменных в атрибуте __code__, 
# который представляет собой откомпилированное тело функции:

print()
print(' -- Локальные переменные функции avg: ---')
print(avg.__code__.co_varnames)

print(' -- Свободные переменные функции avg: ---')
print(avg.__code__.co_freevars)

# Привязка переменной series хранится в атрибуте __closure__ функции avg.
# Каждому элементу avg.__closure__ соответствует имя в avg.__code__.co_freevars. 
# Эти элементы называются ячейками (cells), 
# у каждого из них есть атрибут cell_contents, где можно найти само значение:

print(' -- Привязка свободных переменных функции avg: ---')
print(avg.__closure__)

print(' -- Содержимое первой свободной переменной функции avg: ---')
print(avg.__closure__[0].cell_contents)


# Вторая версия функции make_averager, не хранящая все принятые значения: 

def make_averager():
    count = 0
    total = 0
    def averager(new_value):
        nonlocal count, total       # <- Обязательно указание nonlocal !!!
        count += 1
        total += new_value
        return total / count
    return averager

print()
print(' -- Демонстрация работы второй версии замыкания --')

avg = make_averager()
print(avg(20))
print(avg(21))
print(avg(22))

