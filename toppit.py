import config
import mailer
import postpuller

config = config.load_config()
content = postpuller.pull(['programming'])
mailer.send_today_toppit(config, content)
