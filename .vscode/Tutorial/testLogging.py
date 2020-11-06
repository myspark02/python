import logging
import logging.config
import os
from os import path

import traceback

# from logging.handlers import RotatingFileHandler

from logging.handlers import TimedRotatingFileHandler
import time


import logging
from pythonjsonlogger import jsonlogger

logger = logging.getLogger()

logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)
logger.error("This is error message for json logger")
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)

# s, m, h, d, midnight, w0, w1, ...  : w0 means monday
# handler = TimedRotatingFileHandler('timed_test.log', when='s', interval=5, backupCount=5)

#roll over after 2KB, and keep backup logs app.log.1, app.log.2, etc.
# handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
# logger.addHandler(handler)

# for i in range(6):
# for i in range(10000) :
    # logger.info("Hello World!")
    # time.sleep(5)

# try :
#     a = [1,2,3]
#     val = a[4]
# except :
#     logging.error("The error is %s", traceback.format_exc())    
# except IndexError as e :
#     logging.error(e, exc_info=True)    

# print(path.abspath(__file__))
# print(path.dirname(path.abspath(__file__)))
# print('--------------------')

# log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')

# logging.config.fileConfig(log_file_path)
# print(os.getcwd())
# logger = logging.getLogger('simpleExample')
# logger.debug('this is a debug message')

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(name)s-%(levelname)s-%(message)s', 
#                     datefmt='%m/%d/%Y %H:%M:%S')
# import helper


# logging.basicConfig(filename='example.log',  level=logging.DEBUG)
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')
# logging.error('And non-ASCII stuff, too, like Øresund and Malmö')

# logging.debug("This is a debug message")
# logging.info("This is a info message")
# logging.warning("This is a warn message")
# logging.error("This is a error message")
# logging.critical("This is a critical message")