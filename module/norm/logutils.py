import logging
from norm import timeutils
import os


class Logger(logging.Logger):
    """
    A script logger to save information into a file.
    """
    OPTIONS = 'Options'
    OPTIONS_START = f'..........{OPTIONS}..........'
    OPTIONS_END = OPTIONS_START.replace(OPTIONS, '.' * len(OPTIONS))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setLevel(logging.INFO)
        hdlr = logging.FileHandler(f"{self.name}.log", mode='w')
        hdlr.setFormatter(logging.Formatter('%(message)s'))
        self.addHandler(hdlr)

    def infoJob(self, options):
        self.info(self.OPTIONS_START)
        for key, val in options.__dict__.items():
            self.info(f"{key}: {val}")
        self.info(f"JobStart: {timeutils.Date.now().strftime()}")
        self.info(self.OPTIONS_END)

    def info(self, msg, *args, timestamp=False, **kwargs):
        super().info(msg, *args, **kwargs)
        if timestamp:
            self.info(timeutils.Date.now().strftime())

    @classmethod
    def get(cls, name):
        # Create new or retrieve previous
        logger_class = logging.getLoggerClass()
        logging.setLoggerClass(cls)
        logger = logging.getLogger(os.path.basename(name))
        logging.setLoggerClass(logger_class)
        return logger


class Base:
    """
    A base class with a logger to print logging messages.
    """

    def __init__(self, logger=None, options=None):
        self.logger = logger
        self.options = options

    def info(self, msg, *args, **kwargs):
        if self.logger:
            self.logger.info(msg, *args, **kwargs)
        else:
            print(msg)