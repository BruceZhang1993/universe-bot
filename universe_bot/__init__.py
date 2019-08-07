import sys
from universe_bot.logger import initialize_logger, ensure_dirs

__appname__ = 'Universe Bot'
__version__ = '0.0.1'
__url__ = 'https://github.com/BruceZhang1993/universe-bot'
__author__ = 'Bruce Zhang (BruceZhang1993)'
__license__ = 'GPL3'
__email__ = 'zttt183525594@gmail.com'
__description__ = 'One bot for universe.'
__keywords__ = ['bot', 'telegram', 'irc']

with open("./README.md", "r") as fh:
    __long_description__ = fh.read()

with open('./requirements.txt') as f:
    __requirements__ = [l for l in f.read().splitlines() if l]


def initialize(debug=False):
    try:
        ensure_dirs()
        initialize_logger(debug)
    except Exception as e:
        print('[Exception] ' + str(e))
        sys.exit(1)
