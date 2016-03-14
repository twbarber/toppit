import configparser


def load_config(self):
    config = configparser.ConfigParser()
    config.read('.toppit')
    subreddits = []
    for subreddit in config.get('Subreddits').split(','):
        subreddits.append(subreddit)
    return {
        'email': config.get('Email'),
        'subreddits': subreddits
    }
