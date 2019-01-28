def my_sh_new_decorator(function_to_decorate):
    def the_wrapper_around_the_original_function():
        print("=== Это код, который отрабатывает до вызова функции")
        function_to_decorate()
        print("*** Это код, который отрабатывает после")
    return the_wrapper_around_the_original_function


def stand_alone_function():
    print("Я одинокая функция, не надо менять трогать и изменять")


stand_alone_function()
print()
stand_alone_function_decorated = my_sh_new_decorator(stand_alone_function)
stand_alone_function_decorated()

print()
# а теперь тот же декоратор, но с пом. синт.сахара:

@my_sh_new_decorator
def another_stand_alone_function():
    print("Отвалите от меня!")


another_stand_alone_function()
