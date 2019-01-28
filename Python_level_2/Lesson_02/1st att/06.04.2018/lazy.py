#!/usr/bin/env python3

def add(x, y):

    def fn():

        return x() + y()

    return fn

def mul(x, y):

    def fn():

        return x() * y()

    return fn

def var(value):

    def fn():

        return value

    return fn

x = var(10)
y = var(20)
z = var(30)
ev = add(mul(x, y), z)

print(ev())

