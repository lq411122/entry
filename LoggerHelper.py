import sys, os
import logging
from logging.config import dictConfig
from Configs import APP_TMP_DIR, APP_LOGGING

## config the logging
#log_dir = os.path.join(APP_TMP_DIR, 'logs') ## os.getenv('SYSTEMROOT') + '\\..\\LOTS'
try:
    if not os.path.exists(APP_TMP_DIR):
        os.makedirs(APP_TMP_DIR)
except Exception as exp:
    print('ERROR : Create Dir %s failed.' % APP_TMP_DIR)
    sys.exit(1)

try:
    dictConfig(APP_LOGGING)
except Exception as exp:
    print('%s' % exp)
logger = logging.getLogger('start')

global __FIST_TIME
__FIST_TIME = True

if __FIST_TIME:
    #sys.stderr.write = lambda s: logger.error(s)
    #sys.stdout.write = lambda s: logger.info(s)
    __FIST_TIME = False

if __name__ == '__main__':
    logger.error("test-error")
    logger.info("test-info")
    logger.warning("test-warn")