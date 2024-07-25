import logging
from enum import Enum


class LogLevel(Enum):
    DEBUG = "debug"
    INFO = "info"
    WARNING = "warn"
    ERROR = "error"


class LogHandler(logging.StreamHandler):
    def __init__(self, stream=None):
        super().__init__(stream)
        self.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))


def set_level(log_level: LogLevel) -> None:
    logging.getLogger("carla_doc").setLevel(log_level.value.upper())


def setup(log_level: LogLevel):
    logger = logging.getLogger("carla_doc")
    logger.setLevel(log_level.value.upper())
    for handler in logger.handlers:
        logger.removeHandler(handler)
    logger.addHandler(LogHandler())


def get_logger(name: str = "carla_doc"):
    return logging.getLogger(name)
