import functools


def foo():
    print("foo")


print(foo.__name__)


def bar(func):
    def wrapper():
        print("bar")
        return func()
    return wrapper


@bar
def foo():
    print("foo")


print(foo.__name__)


def bar(func):
    @functools.wraps(func)
    def wrapper():
        print("bar")
        return func()
    return wrapper

@bar
def foo():
    print("foo")

print(foo.__name__)
