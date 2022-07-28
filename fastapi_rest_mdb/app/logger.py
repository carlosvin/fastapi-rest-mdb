

from logging import Logger, StreamHandler
from pythonjsonlogger import jsonlogger


def config_logger(logger: Logger, level: str) -> None:
    logger.setLevel(level)
    log_handler = StreamHandler()
    formatter = jsonlogger.JsonFormatter()
    log_handler.setFormatter(formatter)
    logger.addHandler(log_handler)
    return logger
