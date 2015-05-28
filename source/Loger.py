# coding=utf-8
from datetime import datetime


def log(msg, level="DEBUG"):
    '''
    Funkcja logująca
    :param msg:
    :param level:
    :return:
    '''
    time = str(datetime.now())
    print "%s\t%s\t%s" % (time, level, msg)
