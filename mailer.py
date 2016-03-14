import smtplib
from email.mime.text import MIMEText

fp = open(textfile, 'rb')
msg = MIMEText(fp.read())
fp.close()

msg['Subject'] = 'The contents of %s' % textfile
msg['From'] = me
msg['To'] = you

s = smtplib.SMTP('localhost')
s.sendmail(me, [you], msg.as_string())
s.quit()