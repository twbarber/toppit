import config, mailer, postpuller

conf = config.load_config()
print(config.get('email'))