
# ---------- Организация тестирования сетевых приложений ------------ 
# ----------------   PyTest Monkeypatching   ---------------------

import pytest
import socket

def my_send(sock, msg):
    ''' Функция отправки сообщения в сокет
    '''
    msg = 'message: {}'.format(msg)
    msg = msg.encode('ascii')
    sock.send(msg)


def my_recv(sock, limit):
    ''' Функция получения и базовой обработки сообщения из сокета
    '''
    data = sock.recv(limit)
    return data.split()



class MySocket():
    ''' Класс-заглушка для операций с сокетом
    '''
    def __init__(self, sock_type=socket.AF_INET, sock_family=socket.SOCK_STREAM):
        self.data = b''

    def send(self, data):
        self.data = data
        return len(data)

    def recv(self, n):
        return b'Hello'

# Создадим фикстуру, которая заменяет класс socket
@pytest.yield_fixture
def my_socket():
    orig_sock = socket.socket
    socket.socket = MySocket
    yield
    socket.socket = orig_sock


def test_send(my_socket):
    ''' Тестирование отправки сообщения в сокет с использованием
        пользовательской фикстуры
    '''
    sock = socket.socket()
    my_send(sock, 'Hello')
    assert sock.data == b'message: Hello'


def test_send_data_1(monkeypatch):
    ''' Использование monkeypatching для замены класса socket
    '''
    monkeypatch.setattr("socket.socket", MySocket)
    sock = socket.socket()
    my_send(sock, 'Test Data')
    assert sock.data == b'message: Test Data'


def test_send_data_2(monkeypatch):
    ''' Использование monkeypatching для замены функции socket.send
    '''    
    test_data = b''
    def monkey_send(self, data):
        ''' Функция-эмулятор socket.send
        '''
        nonlocal test_data
        test_data = data
        return len(data) 

    monkeypatch.setattr("socket.socket.send", monkey_send)
    sock = socket.socket()
    my_send(sock, 'Test Data')
    assert test_data == b'message: Test Data'


def test_recv_data(monkeypatch):
    ''' Использование monkeypatching для замены функции socket.recv
    '''    
    def monkey_recv(self, limit):
        ''' Функция-эмулятор socket.recv
        '''
        some_data = b'Hello, this is Monkey!'
        return some_data[:limit]

    monkeypatch.setattr("socket.socket.recv", monkey_recv)
    sock = socket.socket()
    test_data = my_recv(sock, 1024)
    assert test_data == [b'Hello,', b'this', b'is', b'Monkey!']
