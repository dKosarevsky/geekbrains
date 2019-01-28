import json

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

obj = json.load(open('tuple_ex.json'))

print(type(obj))