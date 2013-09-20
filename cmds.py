# cmds.py
#
# doing the commands
#
# Andrej Frank 30.11.2007 GPL

import sys, os, time, socket, popen2

import config, syslog, snort

class cmds:
    def __init__(self):
        self.config=config.config()
        self.infos={}
        self.allcommands=self.config.getallcommands()

#    def isset(self, item):
#        return self.config.isset("commands", item)

    def getallcommands(self):
        return self.allcommands

    def execute(self):
        commands=self.config.getcommands()
        for cmd in commands:
            if "cdate" in cmd:
                self.infos[cmd] = time.asctime()+"\n"
            elif "chostname" in cmd:
                self.infos[cmd] = socket.gethostbyaddr(socket.gethostname())[0]+"\n"
            elif "cuname" in cmd:
                (r,w,e)=popen2.popen3('uname')
                w.close(); e.close()
                self.infos[cmd] = "".join(r.readlines())
                r.close()
            elif "cuptime" in cmd:
                (r,w,e)=popen2.popen3('uptime')
                w.close(); e.close()
                self.infos[cmd] = "".join(r.readlines())
                r.close()
            elif "cdfh" in cmd:
                (r,w,e)=popen2.popen3('df -h')
                w.close(); e.close()
                self.infos[cmd] = "".join(r.readlines())
                r.close()
            elif "cwho" in cmd:
                (r,w,e)=popen2.popen3('who')
                w.close(); e.close()
                self.infos[cmd] = "".join(r.readlines())
                r.close()
            elif "clast" in cmd:
                (r,w,e)=popen2.popen3('last')
                w.close(); e.close()
                self.infos[cmd] = "".join(r.readlines())
                r.close()
            elif "cps" in cmd:
                (r,w,e)=popen2.popen3('ps afux')
                w.close(); e.close()
                self.infos[cmd] = "".join(r.readlines())
                r.close()
            elif "cloging" in cmd:
                self.infos[cmd]=syslog.dologing()
            elif "csnort" in cmd:
                self.infos["csnort"]={}
                self.infos["csnort"]["log"]=snort.snortlog()
                if self.config.isset("snort", "db"):
                    self.infos["csnort"]["db"]=snort.snortdb()
        return self.infos
            

    def printit(self):
        print self.allcommands
        print self.infos['cwho']  



