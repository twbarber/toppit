import smtplib
import time
from email.mime.text import MIMEText


def send_today_toppit(config, message):
    sender = config.email
    password = config.password
    recipients = config.recipients

    session = build_session(sender, password)
    message = build_message(sender, recipients, message)
    session.sendmail(sender, recipients, message.as_string())
    session.quit()


def build_session(user, password):
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.ehlo()
    session.starttls()
    session.login(user, password)
    return session


def build_message(sender, recipients, message):
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Toppit Update: %s' % time.strftime('%x')
    msg['From'] = sender
    msg['To'] = ", ".join(recipients)
    return msg
