import json


# запись, используем method dumps
dict_to_json = {
    "action": "msg",
    "to": "account_name",
    "from": "account_name",
    "encoding": "ascii",
    "message": "message"
    }

with open('mes_example_write.json', 'w') as f_n:
    f_n.write(json.dumps(dict_to_json))

with open('mes_example_write.json') as f_n:
    print(f_n.read())

print()
# но корректнее для записи применять method dump
dict_to_json = {
    "action": "msg",
    "to": "account_name",
    "from": "account_name",
    "encoding": "ascii",
    "message": "message"
    }

with open('mes_example_write_2.json', 'w') as f_n:
    json.dump(dict_to_json, f_n)

with open('mes_example_write_2.json') as f_n:
    print(f_n.read())

print()
# используем параметры sort_keys и indent для выполнения
# сортировки и установки величины отступа
dict_to_json = {
    "action": "msg",
    "to": "account_name",
    "from": "account_name",
    "encoding": "ascii",
    "message": "message"
    }

with open('mes_example_write_3.json', 'w') as f_n:
    json.dump(dict_to_json, f_n, sort_keys=True, indent=2)

with open('mes_example_write_3.json') as f_n:
    print(f_n.read())

print()
# изменение типов данных
tuple_ex = (
    "action",
    "to",
    "from",
    "encoding",
    "message"
    )

print(type(tuple_ex))

with open('tuple_ex.json', 'w') as f_n:
    json.dump(tuple_ex, f_n, sort_keys=True, indent=2)

objs = json.load(open('tuple_ex.json'))

print(type(objs))

print()
# в json нельзя сохранить словарь, где ключи - кортежи
dict_to_json = {
    ('action', 'to'): 'msg',
    'from': 'account_name'
    }

# with open('dict_to_json.json', 'w') as f_n:
#     json.dump(dict_to_json, f_n)
#
# with open('dict_to_json.json') as f_n:
#     print(f_n.read())
#  TypeError: key ('action', 'to') is not a string

# Но! Если юзаем доп.параметр shipkeys - игнорим такие ключи
with open('dict_to_json.json', 'w') as f_n:
    json.dump(dict_to_json, f_n, skipkeys=True)

with open('dict_to_json.json') as f_n:
    f_n_content = f_n.read()
    obj = json.loads(f_n_content)

print(obj)

print()
# ключи в словарях в JSON-формате могут быть только строки
# числа будут преобразованы в строкое представление
d = {
    5: 300,
    1: 400
    }

d_to_json = json.dumps(d)

print(d_to_json)