# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import sys
import os
import shutil
from dz05_easy import create_dir, delete_dir, papki, file_copy


# print(sys.argv)

def main():
    while True:
        print('''            1. Перейти в папку
            2. Просмотреть содержимое текущей папки
            3. Удалить папку
            4. Создать папку
            q. Выход''')
        user_input = input()

        if user_input == 'q':
            print('Всего доброго!')
            break

        elif user_input == '1':
            dirname = input('Введите имя папки: ')
            file_list = papki()
            if dirname in file_list:
                os.chdir(dirname)
                print('Переход в папку {} прошёл успешно'.format(dirname), os.getcwd())
            else:
                print('Папка с таким именем отсутствует!')

        elif user_input == '2':
            dirname = os.getcwd()
            print(os.getcwd(), papki(dirname))

        elif user_input == '3':
            dirname = input('Введите имя папки: ')
            try:
                delete_dir(dirname)
                print('Папка {} успешно удалена'.format(dirname))
                print()
            except FileNotFoundError:
                print('Папка с именем', dirname, 'не найдена!')
                print()
        elif user_input == '4':
            dirname = input('Введите имя папки: ')
            try:
                create_dir(dirname)
                print('Папка {} успешно создана'.format(dirname))
                print()
            except FileExistsError:
                print('Папка с именем', dirname, 'уже существует!')
                print()
        else:
            print('Такого пункта меню нет')
            print()
            continue
main()