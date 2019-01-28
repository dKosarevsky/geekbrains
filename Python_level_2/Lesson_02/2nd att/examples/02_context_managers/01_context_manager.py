
# -------------------- Менеджеры контекста ---------------------------------------

# Как работает оператор with?

# with open('test', 'w') as f:
#     f.write('Stroka')

# Оператор with использует интерфейс менеджера контекста объекта.
# Создадим свой класс, реализующий интерфейс менеджера контекста.    

class ListTransaction:
    def __init__(self, thelist):
        self.thelist = thelist

    def __enter__(self):
        self.workingcopy = list(self.thelist)
        return self.workingcopy

    def __exit__(self, exc_type, value, traceback):
        print(exc_type, value, traceback)
        if exc_type is None:
            self.thelist[:] = self.workingcopy
        return False


items = [1, 2, 3]

with ListTransaction(items) as tr:
    tr.append(4)
    tr.append(5)

print(items) 


try:
    with ListTransaction(items) as working:
        working.append(6)
        working.append(7)
        raise ValueError("Ошибка в транзакции! Данные не будут сохранены")

except ValueError:
    print("Произошёл системный сбой! Проверьте данные!")
    

print(items) 


# Небольшое упрощение с использованием модуля contextlib...

from contextlib import contextmanager


@contextmanager
def ListTransaction(thelist):
    workingcopy = list(thelist)

    yield workingcopy
    # Часть кода после строки yield будет выполнена, если не возникло исключений
    
    # Изменить оригинальный список, только если не возникло ошибок
    print('No exception')
    thelist[:] = workingcopy



items = ['Фродо', 'Сэм', 'Горлум']
try:
    with ListTransaction(items) as working:
        # working = 'l-i-s-t-'
        working.append('Кольцо')
        working.append('Мордор')
        raise(ValueError('oop'))

except ValueError:
    print("Кто-то!")

print(items) 





