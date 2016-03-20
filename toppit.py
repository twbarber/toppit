from toppit import postpuller, message, mailer
from toppit.config import Config

conf = Config()
posts = postpuller.pull(conf.subreddits, conf.interval, conf.count)
content = message.format_message(posts)
mailer.send_today_toppit(conf, content)
