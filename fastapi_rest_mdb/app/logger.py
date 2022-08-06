from logging import Logger, StreamHandler, getLogger
from pythonjsonlogger import jsonlogger


def config_logger(logger: Logger, level: str) -> Logger:
    logger.setLevel(level)
    if logger.handlers:
        log_handler = logger.handlers[0]
    else:
        log_handler = StreamHandler()
        logger.addHandler(log_handler)
    formatter = jsonlogger.JsonFormatter(
        "%(levelname)s %(module)s %(filename)s %(lineno)s %(message)s %(threadName)s",
        timestamp=True,
        static_fields={"log": logger.name},
    )
    log_handler.setFormatter(formatter)
    return logger


def config_loggers(level: str, *logger_names) -> None:
    for logger_name in logger_names:
        config_logger(getLogger(logger_name), level)
