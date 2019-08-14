
import sys
import os
from universe_bot import __appname__, __version__, __description__
from universe_bot.config import Config
from universe_bot.logger import logger
from universe_bot.plugin import register_all_plugins
from universe_bot.backend import available_backends


def application(args):
    if args.version:
        print(__appname__ + ' ' + __version__)
        print(__description__)
        sys.exit(0)
    if args.conf:
        conf = os.path.abspath(args.conf)
    else:
        conf = None
    logger().debug('loading configuration from ' + str(conf))
    Config(conf)
    logger().info('successfully loaded configuration')
    print(register_all_plugins())
    print(available_backends)
    raise NotImplementedError('not implemented')
