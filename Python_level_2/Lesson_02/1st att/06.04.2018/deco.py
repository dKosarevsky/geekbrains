#!/usr/bin/env python3

def deco(f):

    def wrap(*args, **kwargs):

        print("BEFORE", f.__name__)

        res = f(*args, **kwargs)

        print("AFTER")

        return res

    return wrap

@deco
def func(lst):

    return sum(lst)

#func = deco(func)

# 17 - 18 строки - идентичны - 22-й

print(func([1,2,3,4,5,6,7]))

# func(lst = [1,2,3])
# func([1,2,3])
# *args - список всех неименнованных аргументов, которые функция не смогла позиционировать
# **kwargs - словарь всех именнованных аргументов, которые функция не смогла позиционировать
