# coding=utf-8
from datetime import datetime
import constants


def log(msg, level="DEBUG"):
    '''
    Funkcja logująca
    :param msg:
    :param level:
    :return:
    '''
    time = str(datetime.now())
    log_msg = "%s\t%s\t%s" % (time, level, msg)
    if constants.debug:
        print log_msg
    else:
        logfile = open('logs.log', 'a')
        logfile.write(log_msg +"\n")
        logfile.close()
