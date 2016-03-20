from toppit import config, postpuller, message, mailer

conf = config.load_config()
posts = postpuller.pull(conf.get('subreddits'))
content = message.format_message(posts)
mailer.send_today_toppit(conf, content)
