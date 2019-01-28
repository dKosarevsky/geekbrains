import json


dict_to_json = {
    ('action', 'to'): 'msg',
    'from': 'account_name'
    }

with open('dict_to_json.json', 'w') as f_n:
    json.dump(dict_to_json, f_n, skipkeys=True)

with open('dict_to_json.json', 'w') as f_n:
    f_n_content = f_n.read()
    obj = json.loads(f_n_content)
