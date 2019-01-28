#!/usr/bin/env python3

def meta_deco(a):

    def deco(f):

        def wrap(*args, **kwargs):

            print("BEFORE", f.__name__, a)

            res = f(*args, **kwargs)

            print("AFTER")

            return res

        return wrap

    return deco

@meta_deco(10)
def func(lst):

    return sum(lst)

#func = meta_deco(10)(func)

# 17 - 18 строки - идентичны - 22-й

print(func([1,2,3,4,5,6,7]))

