import logging
import otherMod


def main():
    logging.basicConfig(filename="myLog.log", level=logging.INFO)
    logging.info("Программа запустилась")
    result = otherMod.add(7, 8)
    logging.info("Всё отработало корректно")


if __name__ == "__main__":
    main()
