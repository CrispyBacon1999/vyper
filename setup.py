
from distutils.core import setup
setup(name='vyper-bot',
      version='5.0.1',
      author='Josh Bacon',
      author_email='bacon.josh09@gmail.com',
      packages=['vyper',],
      url='https://vyper-bot.readthedocs.io',
      requires=[
            'requests',
            'grequests'
          ],
      description='A telegram API written in pure python.',
      long_description='A telegram API written in pure python, created for beginners, but catering to advanced users. Has many functions built in to make bot creation easier, as well as some prebuilt classes to make starting a breeze.')