import logging
import datetime

def get_logger(options=None):
    logger = logging.getLogger(options.JOBNAME)
    logging.basicConfig(filename=f"{options.JOBNAME}.log", level=logging.INFO, filemode='w')
    return logger

def log_options(options=None, logger=None):
    OPTIONS = 'Options'
    OPTIONS_START = f'..........{OPTIONS}..........'
    OPTIONS_END = OPTIONS_START.replace(OPTIONS, '.' * len(OPTIONS))
    logger.info(OPTIONS_START)
    for key, val in options.__dict__.items():
        if type(val) is list:
            val = ' '.join(map(str, val))
        logger.info(f"{key}: {val}")
    logger.info(f"JobStart: {datetime.datetime.now().strftime('%H:%M:%S')}")
    logger.info(OPTIONS_END)