# class WorkerBuilder:
#     def __init__(self, data):
#         for key, value in data.items():
#             setattr(self, key, value)
#
#
# class Wrapper:
#     def __init__(self, object):
#         self.wrapped = object
#
#     def __getattr__(self, attrname):
#         print('Попытка получить аттрибут {}'.format(attrname))
#         return getattr(self.wrapped, attrname)
#
# worker = WorkerBuilder({'name': 'Ivan', 'age': 20})
# # print(worker.name, worker.age)
#
# wrapper = Wrapper(worker)
# print(wrapper.name)
# print(wrapper.age)


class IncorrectName(Exception):

    def __str__(self):
        return 'IncorrectName: Вы ввели некорректное имя!'


name = input('name: ')
if len(name) < 1:
    raise IncorrectName