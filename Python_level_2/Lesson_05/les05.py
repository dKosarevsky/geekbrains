import logging


log = logging.getLogger("app")

logging.basicConfig(
    filename="app.log",
    format="%(levelname)-10s %(asctime)s %(message)s",
    level=logging.INFO)

log.info('Hello World!')
log.warning("Это возможно баг..")
log.critical("Критическая ошибка в app! "
             "Необходимо исправить!!!")

parms = {'host': 'www.python.org',
         'port': 80}
log.critical("Не могу подключиться к сайту %(host)s через порт %(port)d", parms)
