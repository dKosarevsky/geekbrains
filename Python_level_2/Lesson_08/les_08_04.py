from threading import Thread
from queue import Queue


class WorkerThread(Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.input_queue=Queue()

    def send(self, item):
        self.input_queue.put(item)

    def close(self):
        self.input_queue.put(None)
        self.input_queue.join()

    def rub(self):
        while True:
            item = self.input_queue.get()
            if item is None:
                break
            print(item)
            self.input_queue.task_done()
        self.input_queue.task_done()
        return


w = WorkerThread()
w.start()
w.send("Hello")
w.send("World!!!")
w.close()
