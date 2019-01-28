def a_decorator_passing_arguments(function_to_decorate):
    def wrapper_accepting_arguments(arg1, arg2):
        print("Вау, у меня есть: ", arg1, arg2)
        function_to_decorate(arg1, arg2)
    return wrapper_accepting_arguments


@a_decorator_passing_arguments
def print_full_name(first_name, last_name):
    print("Меня зовут", first_name, last_name)


print_full_name("Серафима", "Анечка")
