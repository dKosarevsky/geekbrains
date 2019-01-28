
# ---- Менеджеры контекста. Различия между менеджером и объектом контекста ----

# Менеджер контекста - это не тот же объект, который возвращается методом __enter__


class LookingGlass:
    def __enter__(self):
        ''' Ради забавы заменим стандартный поток вывода на "реверсивный" '''
        import sys
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'JABBER_WOCKY'

    def reverse_write(self, text):
        ''' В оригинальный поток вывода передается перевёрнутая строка '''
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_value, traceback):
        ''' При выходе из контекста вернём стандартный поток вывода '''
        import sys
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print('Пожалуйста, HE НАДО делить на нуль!')
        return True


with LookingGlass() as what:
    print('Мы находимся в контексте')
    print(what)

print('Код за пределами контекста')
print(what)

