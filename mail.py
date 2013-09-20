# Functions to send mail
# one is a python smtplib function
# the other is sending through "mail" command
#
# Andrej Frank 30.11.2007 GPL

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.Utils import formatdate

import popen2

import config

def send_mail(text):
    """ send_mail(text) - sending mail with text 
        to send_to (is standing in ini-file). """
    conf=config.config()
    send_from=conf.getsender()
    send_to=conf.getreceiver()
    server=conf.getserver()
    subject="INFOS from %s"%conf.gethostID()
    if conf.isset("mail","smtp_python"):
        __send_mail_python(send_from, send_to, subject, text, server)
    else: 
        __send_mail_os(send_to, subject, text)


def __send_mail_python(send_from, send_to, subject, text, server):
    """sending mail with python smtplib"""
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = send_to
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach( MIMEText(text) )
    smtp = smtplib.SMTP(server)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()


def __send_mail_os(send_to, subject, text):
    """sending mail with mail command"""
    (r,w,e)=popen2.popen3('mail -s "%s" %s'%(subject, send_to))
    w.write(text)
    r.close; w.close; e.close

