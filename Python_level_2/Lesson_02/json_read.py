import json


with open('ex_read.json') as f_n:
    objs = json.load(f_n)

for section, commands in objs.items():
    print(section)
    print(commands)

print()
# Используем method loads
with open('ex_read.json') as f_n:
    f_n_content = f_n.read()
    objs = json.loads(f_n_content)

print(objs)

for section, commands in objs.items():
    print(section)
    print(commands)
