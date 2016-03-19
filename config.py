import configparser


def load_config():
    config = configparser.ConfigParser()
    config.read('.toppit')
    subreddits = []
    for subreddit in config.get('toppit', 'Subreddits').split(','):
        subreddits.append(subreddit)
    return dict(email=config.get('toppit', 'Email'), password=config.get('toppit', 'Password'), subreddits=subreddits)
