import yaml


with open('data_read.yaml') as f_n:
    f_n_content = yaml.load(f_n)
print(f_n_content)

print()
# запись данных в yaml
action_list = ['msg_1',
               'msg_2',
               'msg_3'
               ]

to_list = ['account_1',
           'account_2',
           'account_3'
           ]

data_to_yaml = {'action': action_list,
                'to': to_list
                }

with open('data_write.yaml', 'w') as f_n:
    yaml.dump(data_to_yaml, f_n)

with open('data_write.yaml') as f_n:
    print(f_n.read())

print()
# запись в изменённом формате
action_list_2 = ['msg_1',
               'msg_2',
               'msg_3'
               ]

to_list_2 = ['account_1',
           'account_2',
           'account_3'
           ]

data_to_yaml_2 = {'action': action_list_2,
                'to': to_list_2
                }

with open('data_write.yaml_2', 'w') as f_n:
    yaml.dump(data_to_yaml_2, f_n, default_flow_style=False)

with open('data_write.yaml_2') as f_n:
    print(f_n.read())
