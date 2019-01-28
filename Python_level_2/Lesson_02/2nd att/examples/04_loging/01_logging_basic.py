# ------- Журналирование (логгирование) с использованием модуля logging -------
#                             Базовая настройка

import logging

# Быстрая настройка логгирования может быть выполнена так:
logging.basicConfig(
    filename = "app_01.log",
    format = "%(levelname)-10s %(asctime)s %(message)s",
    level = logging.INFO
)

# Для использования логгера его нужно получить/создать функцией getLogger
log = logging.getLogger('basic')

# После этого можно использовать логгирование таким образом
log.debug('There will be debug information')
log.info('Hello, World!')
log.warning('It seems to be a bug...')
log.critical('Critical bug in app! Hello, World!')

# Обратите внимание, что не все сообщения попали в лог-файл. Почему?
