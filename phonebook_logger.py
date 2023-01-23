import logging
import datetime

date = datetime.date.today()
date = f'{date.strftime("%Y")}-{date.strftime("%m")}-{date.strftime("%d")}'

log_file_path = '%s-%s.log' % ("phonebook", date)

logging.basicConfig(level=logging.DEBUG, filename=log_file_path)
logger = logging.getLogger(__name__)

def log(src, msg):
    logger.info(src + " " + msg)