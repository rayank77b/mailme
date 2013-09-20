#!/usr/bin/python
#
# mailme - send information to a receiver
#
#   the most configuration information are in .config.ini
#
# Andrej Frank 30.11.2007 GPL


import config, cmds, mail




# exectue commands and gather information
cmd=cmds.cmds()
infos=cmd.execute()

allcommands=cmd.getallcommands()

# build a message body for email
text=""
for l in allcommands:
    if infos.has_key(l):
        text+="%s:\n%s----------------------------\n\n"%(l, infos[l])

# sending email
mail.send_mail(text)


# now we must set the execution time in ini-file
