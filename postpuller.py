import praw


def get_top_posts(sub):
    r = praw.Reddit(user_agent='toppit test')
    return r.get_subreddit(sub).get_top_from_day(limit=5)


def pull(subreddits):
    sup_posts = {}
    for sub in subreddits:
        sup_posts.update({sub: get_top_posts(sub)})

    content = ""
    for sub in sup_posts.keys():
        content += str(sub) + '\n\n'
        for post in sup_posts.get(sub):
            content += (str(post) + ': ' + str(post.short_link))
            content += '\n'

    return content
