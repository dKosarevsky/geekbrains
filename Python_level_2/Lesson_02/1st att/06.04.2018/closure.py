#!/usr/bin/env python3

def func(x, y):

    return x + y

def closure(x):

    return func(x, 10)

closure_2 = lambda x: func(x, 10)

func(1, 10)
func(5, 10)
func(7, 10)

#############################################################################

def factory(f, y):

    def wrap(x):

        return f(x, y)

    return wrap

closure_10 = factory(func, 10)
closure_20 = factory(func, 20)
closure_30 = factory(func, 30)

