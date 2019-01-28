from socket import *
from random import randint


s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 8888))

while True:
    tm = s.recv(1024)
    print("Текущее время: %s" % tm.decode('ascii'))

s.close
