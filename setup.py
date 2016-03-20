from distutils.core import setup

setup(
    name='toppit',
    version='0.1.0',
    packages=['toppit'],
    url='https://github.com/twbarber/toppit',
    license='MIT',
    author='Tyler Barber',
    author_email='tylerwbarber@gmail.com',
    description='Receive emails for top subreddit posts.',
    install_requires=[
          'praw'
    ]
)
