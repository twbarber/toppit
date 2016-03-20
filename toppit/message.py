import time

LINE_BREAK = '<br>'
DOUBLE_LINE_BREAK = '<br><br>'
OPEN_HTML = '<html><head></head><body>'
CLOSE_HTML = '</body></html>'
HTML_BOLD = '<b>%s</b>'
HYPERLINK = '<a href="%(x)s">%(y)s</a>'


def build(posts):
    content = introduction()
    content += insert_posts(posts)
    content += signature()
    return content


def introduction():
    return HTML_BOLD % 'Your toppit update for: ' + time.strftime('%x') + DOUBLE_LINE_BREAK


def insert_posts(posts):
    content = OPEN_HTML
    for subreddit in sorted(posts):
        content += HTML_BOLD % subreddit.upper() + DOUBLE_LINE_BREAK
        for post in posts.get(subreddit):
            content += append_post(post)
        content += LINE_BREAK
    content += CLOSE_HTML
    return content


def append_post(post):
    content = str(post) + ': '
    if post.is_self:
        content += HYPERLINK % {'x': str(post.short_link), 'y': 'Reddit Link'}
    else:
        content += HYPERLINK % {'x': str(post.url), 'y': 'External Link'}
    content += LINE_BREAK
    return content


def signature():
    return 'With Love, <br>toppit'
