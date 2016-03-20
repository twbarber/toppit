import configparser

from toppit.interval import Interval


class Config:

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('.toppit')
        self.email = config.get('toppit', 'Email')
        self.password = config.get('toppit', 'Password')
        self.subreddits = self.__parse_list(config.get('toppit', 'Subreddits'))
        self.recipients = self.__parse_list(config.get('toppit', 'Recipients'))
        self.interval = Interval[config.get('toppit', 'Interval')]
        self.count = int(config.get('toppit', 'Count'))

    def __parse_list(self, subs):
        values = []
        for val in subs.split(','):
            values.append(val)
        return values

