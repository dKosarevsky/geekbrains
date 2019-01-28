from threading import Thread, Lock
import time


done = Lock()


def idle_release():
    print("Запуск release!")
    time.sleep(5)
    done.release()


done.acquire()

t = Thread(target=idle_release())
t.start()

done.acquire()
print("Странное поведение блокировок в Python")
