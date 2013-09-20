# syslog - collect information from syslog or messages
#
# Andrej Frank 30.11.2007  GPL

import re, time

import config

months={"Nov":11}

def dologing():
    """ dologing() read the information from syslog or message
    which file should taken -> .config.ini -> [logfile]
    logfile=/var/log/syslog.  this should be created by 
    installation script ;)
    next the script should taken only infos that are not older
    as last time excecution. informations which we do not need
    should be filtered (f.e. MARK statements ) 

    the filter are in .config.ini
    [logfile] -> logfilter=(filter1)|(filter2)|(filter3)| ...

    Return: string of Log messages
    """
    loginfos=""
    # Read the path of file
    conf=config.config()
    logfile=conf.getlogfile()
    logfilter=conf.getlogfilter()
    lfilter=re.compile(logfilter)
    
    # find which we are started last time
    lasttime=conf.getlasttime()
    ##print time.ctime(float(lasttime))
    # read and filter the log
    fhl=open(logfile, 'r')
    for line in fhl.readlines():
        zeit=line.split(' ')
        mon=zeit[0]
        day=zeit[1]
        clk=zeit[2]
        clk = clk.split(':')
        timelast=time.mktime([2007, months[mon], int(day), int(clk[0]), int(clk[1]), int(clk[2]),0,0,0])
        if timelast >= float(lasttime): 
            if not lfilter.search(line):
                loginfos+= line

    return loginfos
    
