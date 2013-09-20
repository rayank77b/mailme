mailme
======

mailme - sending status information through mail

This an old project of me, thus maybe dead, use github to store it here.

This programm send status informaiton with mail.
There are: date, uptime, who, lastlog, hostname, syslog, snort ....

This programm is write in python and only few commands are doing by OS (popen2.popen3())


Moduls
    mailme.py              main modul
        config.py          reading configuration (ini-file)  
        cmds.py            commandos
            snort.py       information about snort
            mysql.py       access to mysql
            syslog.py      information about syslog/messages
        mail.py            sending Mail



            Information about INI-File

