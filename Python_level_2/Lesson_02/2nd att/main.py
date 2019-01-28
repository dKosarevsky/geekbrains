# def f():
#     print("i'm function")
#
#
# def g():
#     print("function g")
#
#
# def z():
#     print("function z")
#
#
# def decorator(func):
#     def wrapper():
#         g()
#         func()
#
#     return wrapper
#
#
# print("before")
# f()
#
# f = decorator(f)
#
# print("after")
# f()
#
# z = decorator(z)


# __________________________________________
#
# def add_bread(func):
#     def wrapper():
#         print("up bread")
#         func()
#         print("down bread")
#
#     return wrapper
#
#
# def add_vegetables(func):
#     def wrapper():
#         print("tomato")
#         func()
#         print("salad")
#
#     return wrapper
#
#
# def add_meat():
#     print("meat")
#
# sandwitch_recipe_two = add_bread(add_vegetables(add_bread(add_vegetables(add_meat))))
#
# # sandwitch_recipe_one()
# sandwitch_recipe_two()

# __________________________________________

#
# def add_bread(func):
#     def wrapper():
#         print("up bread")
#         func()
#         print("down bread")
#
#     return wrapper
#
#
# def add_vegetables(func):
#     def wrapper():
#         print("tomato")
#         func()
#         print("salad")
#
#     return wrapper
#
#
# @add_bread
# @add_vegetables
# @add_bread
# @add_vegetables
# def add_meat():
#     print("meat")
#
#
# # sandwitch_recipe_two = add_bread(add_vegetables(add_bread(add_vegetables(add_meat))))
#
# # sandwitch_recipe_one()
# # sandwitch_recipe_two()
#
# add_meat()


# __________________________________________


# def add_bread(func):
#     def wrapper():
#         print("up bread")
#         func()
#         print("down bread")
#
#     return wrapper
#
#
# def add_vegetables(func):
#     def wrapper():
#         print("tomato")
#         func()
#         print("salad")
#
#     return wrapper
#
#
# def print_n_times(n, msg):
#     for i in range(n):
#         print(msg)
#
# def multiply(count):
#     def add_vegetables(func):
#         def wrapper():
#             print_n_times(count, "tomato")
#             print_n_times(count, func())
#             print_n_times(count, "salad")
#
#         return wrapper
#
#     return add_vegetables
#
#
# @multiply(3)
# def add_meat():
#     return "meat"
#
#
# # sandwitch_recipe_two = multiply(5)(add_meat)
#
# # sandwitch_recipe_one()
# # sandwitch_recipe_two()
#
# # sandwitch_recipe_two()
#
# add_meat()
# __________________________________________
#
#
# def decor(func):
#     def wrapper(*args, **kwargs):
#         print("wrapped func")
#         print(func(*args, **kwargs))
#
#     return wrapper
#
#
#
# @decor
# def f(a, b):
#     return f"{a}-{b}"
#
# @decor
# def g(c):
#     return f"{c}"
#
# @decor
# def r(t,y):
#     return f"{t}-{y}"
#
# # f = decor(f)
#
#
# f(2,54)
# g(6)
# r(t="3", y="53")
# __________________________________________


# with open("index.html") as f:
#     print(f.read()[:1000])
#
# print("file closed")
#

# __________________________________________









