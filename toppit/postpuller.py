import praw
from toppit.interval import Interval


def get_top_posts(sub, interval, count):
    r = praw.Reddit(user_agent='toppit test')
    if interval is Interval.DAY:
        return r.get_subreddit(sub).get_top_from_day(limit=count)
    elif interval is Interval.WEEK:
        return r.get_subreddit(sub).get_top_from_week(limit=count)
    elif interval is Interval.MONTH:
        return r.get_subreddit(sub).get_top_from_month(limit=count)
    elif interval is Interval.YEAR:
        return r.get_subreddit(sub).get_top_from_year(limit=count)


def pull(subreddits, interval, count):
    sup_posts = {}
    for sub in subreddits:
        sup_posts.update({sub: get_top_posts(sub, interval, count)})
    return sup_posts


