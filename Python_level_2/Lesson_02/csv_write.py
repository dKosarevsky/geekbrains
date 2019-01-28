import csv


data = [['hostname', 'vendor', 'model', 'location'],
        ['kp1', 'Cisco', '2960', 'Moscow, str'],
        ['kp2', 'Cisco', '2960', 'Novosibirsk, str'],
        ['kp3', 'Cisco', '2960', 'Kazan, str'],
        ['kp4', 'Cisco', '2960', 'Tomsk, str']]

with open('kp_data_write.csv', 'w') as f_n:
    f_n_writer = csv.writer(f_n)
    for row in data:
        f_n_writer.writerow(row)

with open('kp_data_write.csv') as f_n:
    print(f_n.read())

# Тоже самое, но в двойных кавычках
data = [['hostname', 'vendor', 'model', 'location'],
        ['kp1', 'Cisco', '2960', 'Moscow, str'],
        ['kp2', 'Cisco', '2960', 'Novosibirsk, str'],
        ['kp3', 'Cisco', '2960', 'Kazan, str'],
        ['kp4', 'Cisco', '2960', 'Tomsk, str']]

with open('kp_data_write_2.csv', 'w') as f_n:
    f_n_writer = csv.writer(f_n, quoting=csv.QUOTE_NONNUMERIC)
    for row in data:
        f_n_writer.writerow(row)

with open('kp_data_write_2.csv') as f_n:
    print(f_n.read())

# method writerows
data = [['hostname', 'vendor', 'model', 'location'],
        ['kp1', 'Cisco', '2960', 'Moscow, str'],
        ['kp2', 'Cisco', '2960', 'Novosibirsk, str'],
        ['kp3', 'Cisco', '2960', 'Kazan, str'],
        ['kp4', 'Cisco', '2960', 'Tomsk, str']]

with open('kp_data_write_3.csv', 'w') as f_n:
    f_n_writer = csv.writer(f_n, quoting=csv.QUOTE_NONNUMERIC)
    f_n_writer.writerows(data)

with open('kp_data_write_3.csv') as f_n:
    print(f_n.read())

# method DictWriter (with parametr fieldnames)

with open('kp_data_delimiter.csv') as f_n:
    f_n_reader = csv.reader(f_n, delimiter='!')
    for row in f_n_reader:
        print(row)
