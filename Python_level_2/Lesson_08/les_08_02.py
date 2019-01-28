from threading import Thread
import time


def clock(interval):
    while True:
        print("1 - Текущее время: %s" % time.ctime())
        time.sleep(interval)


class ClockThread(Thread):
    def __init__(self, interval):
        super().__init__()
        self.daemon = True
        self.interval = interval

    def run(self):
        while True:
            print("2 -- Текущее время: %s" % time.ctime())
            time.sleep(self.interval)


t = Thread(target=clock, args=(15, ))
t.daemon = True
t.start()

t = ClockThread(2)
t.start()
t.join()
