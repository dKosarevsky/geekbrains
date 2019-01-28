# ------- Журналирование (логгирование) с использованием модуля logging -------
#           Расширенная настройка настройка. Форматирование, обработчики

import logging
import sys

# Определить формат сообщений
_format = logging.Formatter("%(levelname)-10s %(asctime)s %(message)s")

# Создать обработчик, который выводит сообщения с уровнем CRITICAL в поток stderr
crit_hand = logging.StreamHandler(sys.stderr)
crit_hand.setLevel(logging.CRITICAL)
crit_hand.setFormatter(_format)

log = logging.getLogger('basic')

log.addHandler(crit_hand)
log.critical('Oghr! Kernel panic!')