# import sys
# for path in sys.path:
#     print(path)

# import os
#
# print(os.name)
# print(os.getcwd())
# os.mkdir('test')
# os.rmdir('test')
# print(os.path.join('folder', 'subfolder', 'subfoder'))
import sys


def ping():
    print('pong')


def my_help():
    print('Вы можете указать ping или help в качестве аргументов!')


methods = {
    'ping': ping,
    'help': my_help
}

try:
    command = sys.argv[1]
    methods[command]()
except IndexError:
    print('Вы должны указать аргумент!')
except KeyError:
    print('Неверный аргумент, используйте help для справки!')
