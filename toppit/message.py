LINE_BREAK = '<br>'
OPEN_HTML = '<html><head></head><body>'
CLOSE_HTML = '</body></html>'
HTML_BOLD = '<b>%s</b>'


def format_message(posts):
    content = OPEN_HTML
    for subreddit in sorted(posts):
        content += HTML_BOLD % subreddit.upper() + LINE_BREAK + LINE_BREAK
        for post in posts.get(subreddit):
            content += str(post) + ': ' + str(post.short_link) + LINE_BREAK
        content += LINE_BREAK
    content += CLOSE_HTML
    return content
