# class Colors:
#     def __init__(self, colors):
#         self.colors = colors
#
#     def __iter__(self):
#         i = 0
#         while True:
#             yield self.colors[i]
#             i += 1
#             if i == len(self.colors):
#                 i = 0
#
# class Colors2:
#     def __init__(self, colors):
#         self.colors = colors
#         self.i = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.i += 1
#         if self.i == len(self.colors):
#             self.i = 0
#         return self.colors[self.i]
#
# colors = Colors(['red', 'green', 'blue'])
#
# # for color in colors:
# #     print(color, end='')
# #     input()
#
# colors2 = Colors2(['green', 'red', 'white'])
#
# for color in colors2:
#     print(color, end='')
#     input()
#


# f = open('bla')
#
# for line in f:
#     print(line)
#
# f = close('bla')


# import random
#
# class RandNumbers:
#     num = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.num += 1
#         if self.num > 100:
#             raise StopIteration
#         return random.randint(-10, 10)
#
# rnd = RandNumbers()
#
# # for el in rnd:
# #     print('random number = ', el, end='')
# #     input()
# #
# print(list(rnd))
# #
# print(list(rnd))


# import itertools
# #
# # l = iter([1, 2, 3])
# # l1 = iter ([4, 5])
# #
# # for el in itertools.chain(l, l1):
# #     print(el)
# #
# # # for el in itertools.count():
# # #     print(el) # НЕ ЗАПУСКАТЬ!!!
#
# colors = ['red', 'green', 'blue']
#
# for color in itertools.cycle(colors):
#     print(color)
#     input()


# class Vector:
#     def __init__(self, coords):
#         self.x, self.y = coords
#
#     def __add__(self, other):
#         x = self.x + other.x
#         y = self.y + other.y
#         return Vector((x, y))
#
#     def __sub__(self, other):
#         x = self.x - other.x
#         y = self.y - other.y
#         return Vector((x, y))
#
#     def __mul__(self, other):
#         x = self.x * other.x
#         y = self.y * other.y
#         return Vector((x, y))
#
#     def __str__(self):
#         return 'v (%s %s)' %(self.x, self.y)
#
# v1 = Vector((10, 20)) #синтаксический сахар
# #Vector.__init__((10, 20)) #аналогичная запись, вверху синтаксический сахар
# v2 = Vector((11, 21))
#
# v3 = v1 + v2
# #v1.__add__(v2) #аналог, вверху синтСахар
# print(v3.x, v3.y)
#
# v4 = v1 - v2
# print(v4.x, v4.y)
#
# v5 = v1 * v2
# print(v5.x, v5.y)
#
# l = [1, 2, 3]
# # l = list(1, 2, 3) #аналогичная запись, выше синтСахар
#
# a = 2
# # a = int(2) #аналогичная запись, выше синтСахар
#
# # def new():
# #     pass
# #
# # new = def()
#
#
# v1 = Vector((10, 22))
#
# print(v1)
#
# a = 2 + 2.5
# print(a)






# import os
#
#
# class LogReader:
#
#     def __init__(self):
#         self.files = []
#
#         for file in os.listdir():
#             if os.path.isdir(file):
#                 continue
#             if file.startswith('log'):
#                 file_descriptor = open(file, encoding='UTF-8')
#                 self.files.append(file_descriptor)
#
#         self.i = 0
#
#     def __del__(self):
#         for file_descriptor in self.files:
#             file_descriptor.close()
#         print('Файлы закрыты')
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while self.i < len(self.files):
#             for line in self.files[self.i]:
#                 return line
#             self.i += 1
#         raise StopIteration
#
#
# log_reader = LogReader()
#
# for i in log_reader:
#     print(i.strip())

