
import select

sock = [ ... ] # Дочерние сокеты

while True:

    ready_for_read, ready_for_write, _ = select.select(sock, sock, [], timeout = 1)

    for s in ready_for_read:

        s.recv(1024)

