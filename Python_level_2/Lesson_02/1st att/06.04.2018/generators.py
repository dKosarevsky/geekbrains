import sys

def get_numbers(start, end, step):
    while start < end:
        yield start
        start += step

gen = get_numbers(0, 10, 1)

print(list(gen))

try:
    gen = get_numbers(1, 5, 2)
    for i in gen:
        print(i)
except StopIteration as e:
    print(e)