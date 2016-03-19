import smtplib
import time
from email.mime.text import MIMEText


def send_today_toppit(config, message):
    sender = config.get('email')
    password = config.get('password')
    recipient = sender

    session = build_session(sender, password)
    message = build_message(sender, recipient, message)
    session.sendmail(sender, recipient, message.as_string())
    session.quit()


def build_session(user, password):
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.ehlo()
    session.starttls()
    session.login(user, password)
    return session


def build_message(sender, recipient, message):
    msg = MIMEText(message)
    msg['Subject'] = 'Toppit Update: %s' % time.strftime('%x')
    msg['From'] = sender
    msg['To'] = recipient
    return msg
