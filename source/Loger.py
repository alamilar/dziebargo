from datetime import datetime 
def log(msg, level="DEBUG"):
    time = str(datetime.now())
    print "%s\t%s\t%s" % (time, level, msg)