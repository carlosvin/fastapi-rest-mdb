

from logging import Logger, StreamHandler, getLogger
from sys import prefix
from pythonjsonlogger import jsonlogger


def config_logger(logger: Logger, level: str) -> Logger:
    logger.setLevel(level)
    if logger.handlers:
        log_handler = logger.handlers[0]
    else:
        log_handler = StreamHandler()
        logger.addHandler(log_handler)
    formatter = jsonlogger.JsonFormatter(timestamp=True)
    log_handler.setFormatter(formatter)
    return logger


def new_logger(package: str, level: str) -> Logger:
    logger = getLogger(package)
    config_logger(logger, level)
    logger.info("initialized!", extra={"foo": "bar"})
    return logger

def config_uvicorn_loggers(level: str) -> None:
    loggers = ["uvicorn.access", "uvicorn.error", "fastapi"]
    for logger in loggers:
        config_logger(getLogger(logger), level)