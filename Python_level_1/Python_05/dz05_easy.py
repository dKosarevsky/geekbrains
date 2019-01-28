# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.



import os

path_dir = [('dir_' + str(i + 1)) for i in range(9)]

def create_dir(paths):
    if __name__ == "__main__":
        dir_path = os.path.join(os.getcwd(), paths)
        os.mkdir(dir_path)

for i in path_dir:
    try:
        create_dir(i)
    except FileExistsError:
        print(i, 'Папка с таким именем уже существует!')

def delete_dir(paths):
    if __name__ == "__main__":
        dir_path = os.path.join(os.getcwd(), paths)
        os.rmdir(dir_path)

for i in path_dir:
    try:
        delete_dir(i)
    except FileNotFoundError:
        print(i, 'Папка с таким именем не найдена!')




# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# papki = [i for i in os.listdir(path='.') if os.path.isdir(i)]
# print(papki)

def papki(main_path):
    for _ in os.listdir(main_path):
        print(_)
main_path = os.getcwd()

#papki(main_path)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

print()
import shutil

file_copy = os.path.abspath(__file__)

try:
    shutil.copy(file_copy, os.getcwd())
except shutil.SameFileError:
    print('Файл с таким названием уже существует.\nCоздаём копию файла.')
    shutil.copy(file_copy, (os.path.splitext(file_copy)[0])+'_COPY.py')

