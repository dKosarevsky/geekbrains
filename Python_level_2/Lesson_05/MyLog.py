import logging
import otherMod2


def main():
    logger = logging.getLogger("exampleApp")
    logger.setLevel(logging.INFO)

    fh = logging.FileHandler("new_water.log")

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)

    logger.addHandler(fh)

    logger.info("Программа запустилась")
    result = otherMod2.add(7, 8)
    logger.info("Всё отработало корректно")


if __name__ == "__main__":
    main()
