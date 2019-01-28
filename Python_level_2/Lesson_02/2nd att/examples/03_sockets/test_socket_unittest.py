
# ---------- Организация тестирования сетевых приложений ------------ 
# ----------------   mock-объекты unittest    ---------------------

from unittest import mock, TestCase
import socket


class MyClass:
    ''' Класс, работающий с сокетами. 
        Должен быть подвергнут тестированию.
    '''
    def __init__(self):
        self.tcp_socket = socket.socket()
        self.tcp_socket.connect('0.0.0.0', '6767')


class SocketTest(TestCase):
    def test_connect(self):
        # Замена сокета на mock-объект
        with mock.patch('socket.socket') as mock_socket:

            c = MyClass()
            c.tcp_socket.connect.assert_called_with('0.0.0.0', '6767')

    def test_recv(self):
        # Замена сокета на mock-объект
        with mock.patch('socket.socket') as mock_socket:
            # Подстановка значения в качестве результата recv
            mock_socket.return_value.recv.return_value = b'This is Mock-object'

            c = MyClass()

            # Намеренно создадим ошибку
            self.assertEqual(c.tcp_socket.recv(1024), b'This is real data!')
