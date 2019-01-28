# otherMod.py
import logging


def add(x, y):
    logging.info("Сумма %s и %s равна %s" %(x, y, x+y))
    return x + y
