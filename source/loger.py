# coding=utf-8
# pylint: disable=relative-import
"""
Moduk Logera
"""


from datetime import datetime
import constants

def log(msg):
    """
    Funkcja logująca
    :param msg:
    :return:
    """
    time = str(datetime.now())
    log_msg = "%s\t%s" % (time, msg)
    if constants.LOG_LEVEL == "all":
        print log_msg
    else:
        logfile = open('logs.log', 'a')
        logfile.write(log_msg + "\n")
        logfile.close()
