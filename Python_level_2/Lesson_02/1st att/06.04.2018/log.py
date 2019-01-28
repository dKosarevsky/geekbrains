#!/usr/bin/env python3

import logging
import logging.handlers

# Получаем описатель логгера с названием test_log (логгер по умолчанию - logging.getLogger() )
logger = logging.getLogger("test_log")

# Конструируем файловое хранилище лога
fn = logging.FileHandler("log.log")
fn.setLevel(logging.DEBUG)

# Конструируем форматную строку - то, как будут записыватся сообщения в лог, если лог будет хранится в файле
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s ")
fn.setFormatter(formatter)

# Присоединяем хранилище к логгеру
logger.addHandler(fn)
logger.setLevel(logging.DEBUG)

##########################

logger.info("TODO")
logger.debug("TODO - D")
logger.error("TODO - E")

