
fl = open("file.txt")
fl.read(1024)
fl.close()

#############################################################################

with open("file.txt") as fl:

    fl.read(1024)
    fl.read(1024)

#############################################################################

class CWith():

    def __init__(self):

        self.__db = our_bd.open()

    def __enter__(self):

        # Инициализация

        self.__db.start_transaction()

        return self.__db.cursor()

    def __exit__(self, err, value, tb):

        self.__db.commit()

conn = CWith()

with conn as cursor:

    cursor.insert(...)
    cursor.update(...)

