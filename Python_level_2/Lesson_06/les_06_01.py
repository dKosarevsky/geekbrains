def bread(func):
    def wrapper():
        print()
        func()
        print("<\___________/>")
    return wrapper


def ingredients(func):
    def wrapper():
        print("#огурцы#")
        func()
        print(" салат ")
    return wrapper


def sandwich(food="--мясо--"):
    print(food)


# sandwich()
# sandwich = bread(ingredients(sandwich))
# sandwich()


@bread
@ingredients
def sandwich(food="--мясо--"):
    print(food)


sandwich()
