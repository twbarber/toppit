import configparser

conf = None


def get_sender_email():
    global conf
    return conf.get('toppit', 'Email')


def get_sender_password():
    global conf
    return conf.get('toppit', 'Password')


def get_recipients():
    global conf
    recipients = []
    for recipient in conf.get('toppit', 'Recipients').split(','):
        recipients.append(recipient)
    return recipients


def get_subreddits():
    global conf
    subreddits = []
    for subreddit in conf.get('toppit', 'Subreddits').split(','):
        subreddits.append(subreddit)
    return subreddits


def get_interval():
    global conf
    return conf.get('toppit', 'Interval')


def get_count():
    global conf
    return conf.get('toppit', 'Count')


def load_config():
    global conf
    config = configparser.ConfigParser()
    conf = config.read('.toppit')
    email = get_sender_email()
    password = get_sender_password()
    subreddits = get_subreddits()
    recipients = get_recipients()
    interval = get_interval()
    count = get_count()
    return dict(email=email,
                password=password,
                subreddits=subreddits,
                recipients=recipients,
                interval=interval,
                count=count)
