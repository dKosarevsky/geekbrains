import socket


HOST = 'localhost'
PORT = 9999

print('Клиент игры "Виселица" приветствует Вас!')
print('Подключение к серверу {}:{}'.format(HOST, PORT))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

sock.sendall(bytes("START", "utf-8"))

data = sock.recv(1024).decode()
data = data.split(';')

if data[0] == 'GUESS':
    print('Угадайте число от {} до {}. У вас 10 попыток'.format(data[1], data[2]))

    while True:
        x = input('Ваш ответ: ')
        if x == 'q':
            sock.sendall(bytes('GOODBYE', 'utf-8'))
            break

        sock.sendall(bytes('TRY;{}'.format(x), 'utf-8'))
        data = sock.recv(1024).decode()
        data = data.split(';')

        if data[0] == 'TRUE':
            print('Вы угадали')
            break
        elif data[0] == 'FALSE':
            if data[1] == 'MORE':
                print('Вы не правы. Ещё есть попытки...')
                print('Подсказка: больше.')
            elif data[1] == 'LESS':
                print('Вы не правы. Ещё есть попытки...')
                print('Подсказка: меньше.')
        elif data[0] == 'FAIL':
            print('Вы не угадали! =(')
            break


sock.sendall(bytes("GOODBYE", "utf-8"))
sock.close()
