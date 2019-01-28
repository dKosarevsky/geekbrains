class Basket(object):
    def __init__(self, size):
        self.size = size

    def change_size(self, size):
        self.size = size

    def get_size(self):
        print('This Basket size is {}'.format(self.size))

    def put_inside(self, garbage):
        if garbage.size <= self.size:
            print('{} is in Basket'.format(garbage))
        else:
            print('{} is to big for a Basket with size = {}'.format(garbage, self.size))

class Box(Basket):
    def get_size(self):
        print('This Box size is {}'.format(self, size))

    def put_inside(self, garbage):
        if garbage.size <= self.size:
            print('{} is in Box'.format(garbage))
        else:
            print('{} is to big for a Box with size = {}'.format(garbage, self.size))

class Thing(object):
    def __init__(self, size):
        self.size = size

box1 = Basket(40)
box1.get_size()

bag1 = Box(118)
bag1.get_size()

garbage1 = Thing(10)
garbage2 = Thing(50)
garbage3 = Thing(180)

box1.put_inside(garbage1)
box1.put_inside(garbage2)

bag1.put_inside(garbage2)
bag1.put_inside(garbage3)