import time

def decorator(func):

    def fake(value):
        start = time.clock()
        result = func(value)

        end = time.clock()
        print('Time is', end - start)
        return result

    return fake

@decorator
def my_str(value):
    time.sleep(5)
    return str(value)


print(my_str(123))
print(my_str([]))
print(my_str({}))