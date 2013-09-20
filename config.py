#!/usr/bin/python
#
# Liest die Konfigurationsinfos ein
#
# Andrej Frank 29.11.2007 GPL

import sys, string

import ConfigParser


class config:
    def __init__(self, file=".config.ini"):
        self.conf=ConfigParser.ConfigParser()
        self.conf.read(file)

    def printm(self):
        for section in self.conf.sections():
            print section
            for opt in self.conf.options(section):
                print " ", opt, "=", self.conf.get(section, opt)

    def getlogfile(self):
        try:
            return self.conf.get("logfile", "logfile")
        except:
            print "ERROR: There is no Inifile or Section for logfile-logfile"
            sys.exit(-1)

    def getlogfilter(self):
        try:
            return self.conf.get("logfile", "logfilter")
        except:
            print "ERROR: There is no Inifile or Section for logfile-logfilter"
            sys.exit(-1)

    def getlasttime(self):
        try:
            return self.conf.get("executiontime", "lasttime")
        except:
            print "ERROR: There is no Inifile or Section for executiontime-lasttime"
            sys.exit(-1)

    def isset(self, section, item):
        try: 
            answer=self.conf.get(section, item)
            if "yes" in answer:
                return 1
            else:
                return 0
        except:
            print "ERROR: There is no Inifile or Section for %s - %s"%(section, item)
            sys.exit(-1)

    def getcommands(self):
        list=[]
        for opt in self.conf.options("commands"):
            answ=self.conf.get("commands", opt)
            if "yes" in answ:
                list.append(opt)
        return list
                
    def getallcommands(self):
        allcmds=self.conf.get("commands", "allcommands")
        return allcmds.split(',')

    def getreceiver(self):
        try:
            return self.conf.get("mail", "receiver")
        except:
            print "ERROR: There is no Inifile or Section for mail-receiver"
            sys.exit(-1)

    def getsender(self):
        try:
            return self.conf.get("mail", "sender")
        except:
            print "ERROR: There is no Inifile or Section for mail-sender"
            sys.exit(-1)
    
    def gethostID(self):
        try:
            return self.conf.get("mail", "host_identification")
        except:
            print "ERROR: There is no Inifile or Section for mail-host_identification"
            sys.exit(-1)

    def getserver(self):
        try:
            return self.conf.get("mail", "server")
        except:
            print "ERROR: There is no Inifile or Section for mail-server"
            sys.exit(-1)


