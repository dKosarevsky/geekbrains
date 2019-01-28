# for i in range(10):
#     print(i)

# print(max([1,2,3,4,5,100]))
# print(abs(-100))
# print(round(1.1111111, 2))


# def greet(first_name):
#     if first_name:
#         print('Привет, {}'.format(first_name))
#     else:
#         no_name_greet()
#
#
# def no_name_greet():
#     no_name = 'Гость'
#     print('Привет {}!'.format(no_name))
#
#
# greet('Иван')
# greet('')
# no_name_greet()


# def my_summ(a, b):
#     if a > b:
#         return a + b
#     else:
#         return b - a
#
# result = my_summ(1, 5)
#
# def my_while(i):
#     while True:
#         if i > 10:
#             break
#         else:
#             i += 1
#     print('Цикл закончился, функция продолжает работать')


# access = True
#
# if access:
#     def render(name):
#         return 'Welcome, {}'.format(name)
# else:
#     def render(name):
#         return '{}, sorry. Try to enter again.'.format(name)
#
# print(render('Иван'))

# def greetings(name='Гость'):
#     print('Привет, {}'.format(name))
#
#
# greetings('Иван')
# greetings()

# def my_summ(*args):
#     print(args)
#     for i in args:
#         print(i)
#
#
# # my_summ(1, 2, 3, 4)
# a = (1, 2, 3, 4)
# b = [5, 6, 7, 8]
# my_summ(a, *b)


# def my_test(name, email='guest@guest', *args, **kwargs):
#     print(kwargs)
#
#
# human = {'name': 'Ivan', 'age': 20}
# my_test(name='Ivan', age=20)
# my_test(**human)

# def test(x):
#     return x * 2
#
#
# a = lambda x: x * 2 + test(2)
# print(a(5))
# print(test(5))
#
#
# my_list = [1, 2, -3, 4, 5]
# print(tuple(map(lambda x: x * 2, my_list)))
# print(tuple(map(test, my_list)))
#
# result = []
# for i in my_list:
#     result.append(i * 2)
#
# print(tuple(filter(lambda x: x > 0, my_list)))
#
# result = []
# for i in my_list:
#     if i > 0:
#         result.append(i)

names = ['Ivan', 'Olga']
salary = [100, 200, 300]
print(list(zip(names, salary)))
print(dict(zip(names, salary)))

file = open('1.txt', 'r', encoding='UTF-8')
for line in file:
    print(line)
file.close()

# file = open('100.txt', 'a+', encoding='UTF-8')
# file.write('some info')
# file.close()

# with open('154545.txt', 'rb') as file:
#     for line in file:
#         print(line)


