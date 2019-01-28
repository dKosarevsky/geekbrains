
# -------------- Декораторы ----------------------------------
# Декораторы - это фукнции, которые дополняют/модернизируют
# поведение других классов/функций/методов

# Реализуем функцию-декоратор для логгирования аргументов и результата функции,
# к которой он будет применён:
def log(func):

    def decorated(*args, **kwargs):
        res = func(*args, **kwargs)
        print('{}({}, {}) = {}'.format(func.__name__, args, kwargs, res))
        return res

    return decorated    


# Декоратор также может быть реализован в виде класса:
class Log():
    def __init__(self):
        pass

    # Магический метод __call__ позволяет обращаться к объекту класса, как к функции
    def __call__(self, func):
        def decorated(*args, **kwargs):
            res = func(*args, **kwargs)
            print('log2: {}({}, {}) = {}'.format(func.__name__, args, kwargs, res))
            return res

        return decorated

# Чтобы применить декоратор к функции нужно воспользоваться синтаксисом
# @имя_декоратора:

@log                # <- такая запись будет аналогична записи  func = log(func) 
def func(a, b):
    return a * b

@Log()              # <- такая запись будет аналогична записи  func2 = Log()(func2) 
def func2(a, b):
    return a ** b

# func = log(func)    
# func2 = log2(func2)    

# Теперь функции имеют дополнительный функционал:
print('-- Функции с декораторами --')
func(14, 15)        
func2(4, 5)


print()
# К одной функции можно применять несколько декораторов, 
# тогда каждый декоратор записывается на отдельной строке

@log
@log2
def summ(a, b):
    return a + b

print('-- Функция с несколькими декораторами --')
summ(19, 18)