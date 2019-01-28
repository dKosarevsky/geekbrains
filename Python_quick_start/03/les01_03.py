# coding: utf-8

# Python. Быстрый старт.
# Занятие 3.

# Домашнее задание: 
#                  функциями dir и help исследовать модули os, sys, psutil
#                  вывести максимум информации о системе (ветка №2):
#                    имя текущей директории, платформа (ОС), кодировка файловой системы,
#                    логин пользователя, количество CPU


# Подключение модуля производится командой import.
# Модуль os идет в комплекте с Python'ом.
import os

# psutil - сторонний модуль, нужно установить через pip install psutil
import psutil       
import sys

print("Serafima Soft")
print("Привет, программист!")
name = input("Ваше имя: ")

print(name, ", добро пожаловать в мир Python!")

answer = input("Давайте поработаем? (Y/N)")
     
if answer == 'Y' or 'y':
    print("Отлично, хозяин!")
    print("Я умею:")
    print(" [1] - выведу список файлов")
    print(" [2] - выведу информацию о системе")
    print(" [3] - выведу список процессов")
    print(" [4] - выведу кодировку файловой системы")
    print(" [5] - выведу имя текущей директории")
    print(" [6] - выведу имя пользователя")
    print(" [7] - выведу имя системы")
    print(" [8] - выведу инфо об использовании диска")
    print(" [9] - выведу инфо об использовании диска")
    do = int(input("Укажите номер действия: "))
    
    if do == 1:
        print(os.listdir())
    elif do == 2:
        print(sys.platform)
    elif do == 3:
        print(psutil.pids())
    elif do == 4:
        print(sys.getfilesystemencoding())
    elif do == 5:
        print(os.getcwd())
    elif do == 6:
        print(os.getlogin())
    elif do == 7:
        print(os.sysname)                 # не работает #
    elif do == 8:
        print(psutil.disk_usage('/'))
    elif do == 9:
        print(psutil.cpu_count())
    else:
        pass
   
# Функция type выводит информацию о типе переменной (объекта)
# Функция dir показывает внутреннее содержимое переменной (объекта) - атрибуты, методы
# Функция help выводит встронную справку об объекте
    
elif answer == 'N' or 'n':
    print("До свидания!")
else:
    print("Неизвестный ответ")    