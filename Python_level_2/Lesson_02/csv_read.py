import csv


with open('data.csv') as f_n:
    f_n_reader = csv.reader(f_n)
    for row in f_n_reader:
        print(row)

print()
with open('data.csv') as f_n:
    f_n_reader = csv.reader(f_n)
    print(f_n_reader)

print()
with open('data.csv') as f_n:
    f_n_reader = csv.reader(f_n)
    print(list(f_n_reader))

print()
with open('data.csv') as f_n:
    f_n_reader = csv.reader(f_n)
    f_n_headers = next(f_n_reader)
    print('Headers: ', f_n_headers)
    for row in f_n_reader:
        print(row)

# Почему выводит не словарь а OrderedDict?
print()
with open('data.csv') as f_n:
    f_n_reader = csv.DictReader(f_n)
    for row in f_n_reader:
        print(row)
        # print(row['hostname'], row['model'])
