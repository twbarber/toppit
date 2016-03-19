import config
import mailer
import postpuller

conf = config.load_config()
content = postpuller.pull(conf.get('subreddits'))
mailer.send_today_toppit(conf, content)
