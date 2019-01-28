import logging
import sys


app_log = logging.getLogger("app")
app_log.setLevel(logging.INFO)
app_log.propagate = False

app_log.addHandler(logging.FileHandler("app.log"))
app_log.addHandler(logging.StreamHandler(sys.stderr))

app_log.critical("Галактика в опасности! Срочно устраняем баг!!")
app_log.info("Абырвалг!")
