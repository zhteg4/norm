import logging
import datetime

OPTIONS = 'Options'
OPTIONS_START = f'..........{OPTIONS}..........'
OPTIONS_END = OPTIONS_START.replace(OPTIONS, '.' * len(OPTIONS))

def get_logger(options=None):
    logger = logging.getLogger(options.JOBNAME)
    logging.basicConfig(filename=f"{options.JOBNAME}.log", level=logging.INFO, filemode='w')
    return logger

def log_options(options=None, logger=None):
    logger.info(f'..........{OPTIONS}..........')
    for key, val in options.__dict__.items():
        if isinstance(val, list):
            val = ' '.join(map(str, val))
        logger.info(f"{key}: {val}")
    logger.info(f"JobStart: {datetime.datetime.now().strftime('%H:%M:%S %m/%d/%Y')}")
    logger.info(OPTIONS_END)