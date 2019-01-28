# class MyResume(object):
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address
#         self.set_data()
#
#
# class MyResume(object):
#
#




# class Account(object):
#     __slots__ = ['name', 'balance']
#     ...
#
# acc = Account()
# acc.x = 13




class BasicClass(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

bc = BasicClass(13, 42)
print(bc.__dict__)

bc.z = 777
print(bc.__dict__)


class StrictClass(object):
    __slots__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

sc = StrictClass(13, 42)
sc2 = StrictClass(11, 56)

print(dir(sc))
print(sc.__slots__)

print(sc.x, sc.y, sc2.x, sc2.y)

print(sc.__dict__)

