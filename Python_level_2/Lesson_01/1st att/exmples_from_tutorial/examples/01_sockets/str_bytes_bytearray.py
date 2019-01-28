
# В Python 3 все строки - строки юникода
s = 'Python'

# Отдельный тип - строка байтов
bs = b'Python'

# Отдельный тип - bytearray - изменяемая строка байтов
ba = bytearray(bs)

# Преобразования между строками
s2 = bs.decode('cp1251')        # Из байт-строки в юникод строку
bs2 = s.encode('koi8-r')        # Из юникод-строки в строку байтов
ba2 = bytearray(s, 'utf-8')     # Из юникод-строки в массив байтов
