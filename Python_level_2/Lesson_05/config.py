[loggers]
keys=root, exampleApp

[handlers]
keys=fileHandler, consoleHandler

[formatters]
keys=myFormatter

[logger_root]
level=CRITICAL
handlers=consoleHandler

[logger_exampleApp]
level=INFO
handlers=fileHandler
qualname=exampleApp

[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=myFormatter
args=(sys.stdout,)

[handle_fileHandler]
class=FileHandler
formatter=myFormatter
args=("config.log",)

[formatter_myFormatter]
format= %(asctime)s - %(name)s - %(levelname)s - %(message)s
datefmt= %m/%d/%Y %I:%M:%S %p
