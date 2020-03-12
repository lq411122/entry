import os, sys

# This is my base path
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
# all tmp dir dirs
APP_TMP_DIR = os.path.join(BASE_PATH, 'tmp')

# determine if application is a script file or frozen exe
if getattr(sys, 'frozen', False):
    BASE_PATH = sys._MEIPASS
    APP_TMP_DIR = os.path.join(BASE_PATH, '..', 'tmp')
if not BASE_PATH in sys.path:
    sys.path.append(BASE_PATH)

PORT = 8080
ARGS = 'runserver --noreload 0.0.0.0:%d' % PORT
PROCESS_ID = 'code.exe'

APP_LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {  # 格式器
        'standard': {  # 详细
            'format': '[%(asctime)s|%(levelname)s|%(processName)s|%(module)s|%(lineno)s]: %(message)s',
            #'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        'start': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(APP_TMP_DIR, 'start.log'),
            'when': 'D',
            'interval': 1,
            'backupCount': 3,
            'formatter': 'standard',
        },
    },
    'loggers': {
        'start': {
            'handlers': ['start'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

ROOT_URL = 'http://0.0.0.0:8800/'
# 主程序中主页的url
INDEX_URL = '%sstatic/index.html' % ROOT_URL