

from logging import Logger, StreamHandler, getLogger
from pythonjsonlogger import jsonlogger


def config_logger(logger: Logger, level: str) -> Logger:
    logger.setLevel(level)
    log_handler = StreamHandler()
    formatter = jsonlogger.JsonFormatter()
    log_handler.setFormatter(formatter)
    logger.addHandler(log_handler)
    return logger


def new_logger(package: str, level: str) -> Logger:
    logger = getLogger(package)
    config_logger(logger, level)
    logger.info("initialized!")
    return logger

def config_uvicorn_loggers(level: str) -> None:
    loggers = ["uvicorn.access", "uvicorn.error",]
    for logger in loggers:
        config_logger(getLogger(logger), level)