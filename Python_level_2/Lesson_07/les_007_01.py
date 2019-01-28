from socket import *


nbs = socket(AF_INET, SOCK_STREAM)
client_list = []
nc = 2
for j in range(nc):
    (client, ap) = nbs.accept()
    client.setblocking(0)
    client_list.append(client)
