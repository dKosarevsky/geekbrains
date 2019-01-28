s = [1, 2]
v = ['a', 'b']

def myreduce(func, array, initial = 0):
    for item in array:
        result = func(item)

z = myreduce