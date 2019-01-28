# def my_sum(a, b):
#     return a + b
#
#
# print(my_sum(3, 5))
#
# my_function_object = my_sum
#
# # del my_sum
# # my_sum(1, 3)
# print(my_function_object(5, 6))




def say_me_hello():
    # внутри определим функцию
    def hello():
        return 'Hello World!'

    return hello()

# print(say_me_hello())
# # print(hello()) # видна только внутри функции

def my_calc(operator):
    def my_sum(first = 7, second = 5):
        return first + second

    def my_diff(first = 7, second = 5):
        return first - second

    if operator == '+':
        return my_sum

    # не использую (), нам не нужно вызывать функцию
    if operator == '-':
        return my_diff

calc_sum = my_calc('+')

print(calc_sum())
print(my_calc('+')())
print(my_calc('-')())




def say_me_hello():
    # внутри определим функцию
    def hello():
        return 'Hello World!'

    return hello()

def do_somth_w_hello(function):
    print('i do another code')
    print(function())

do_somth_w_hello(say_me_hello)


def my_simple_decorator(func_to_decor):

    def wrapper_arround_our_func():
        # Внутри себя декоратор определяет функцию обертку
        # Она будет обернута вокруг декорируемой
        # получая возможность исполнять произвольный код до и после

        print('я код, который выполняется ДО выполнения func_to_decor')

        func_to_decor()

        print('я код, который выполняется ПОСЛЕ выполнения func_to_decor')

    return wrapper_arround_our_func

@my_simple_decorator
def stable_function():
    print('Hello world!')

# stable_function_decorated = my_simple_decorator(stable_function)
# @my_simple_decorator перед def stable_function():  то же что и запись вверху
print(stable_function())




