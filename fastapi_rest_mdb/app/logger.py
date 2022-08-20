import structlog
import logging
from structlog.processors import JSONRenderer

def config_logger(level: str) -> logging.Logger:
    int_level = logging.getLevelName(level)
    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.processors.add_log_level,
            structlog.processors.StackInfoRenderer(),
            structlog.dev.set_exc_info,
            structlog.processors.TimeStamper(),
            JSONRenderer(indent=1, sort_keys=True)
        ],
        wrapper_class=structlog.make_filtering_bound_logger(int_level),
        context_class=dict,
        logger_factory=structlog.PrintLoggerFactory(),
        cache_logger_on_first_use=False
    )
    structlog.get_logger().info('Hello')
