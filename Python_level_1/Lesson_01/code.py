welcome = 'Hello world!'
style = 'PEP-8'
TELEGRAM_ID = '2gf823gd823d9238yd'
welcome = 100
welcome = 1.1
Welcome = 200
a = 5
b = 10
is_admin = False
is_god = True
asd = True
my_list = [1, 2, 3, 4, 4, 4, 'Cat', is_admin]
my_tuple = ('Anna Semenova', 'Oleg Smirnov')
my_dict = {'name': 'Oleg', 'age': 20}

my_list[0] = 100
my_dict['name'] = 'Anna'

# print(my_list)
# print(my_dict['name'])

# age = int(input('Введите ваш возраст:'))
# print('Ваш возраст:', age + 5)

# is_admin = False
# name = input('Введите ваше имя:')
# password = input('Введите пароль')
# admin_name = 'Admin'
# admin_password = '123456'
#
# if name == admin_name:
#     print('Вы админ!')
#     is_admin = True
# elif name == 'user':
#     print('Добро пожаловать, пользователь!')
# else:
#     print('Вы гость!')
#
#
# if is_admin:
#     print('Здравствуй владелец!')

number = 1
while number < 11:
    if number > 5:
        break
    elif number == 3:
        number += 1
        print('Код перед continue')
        continue
        print('Код после continue')
    else:
        print('Не больше 5 и не равно 3')
    print(number)
    # start_number = start_number + 1
    number += 1
