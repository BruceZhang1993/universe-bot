import argparse
import sys
from universe_bot import initialize, __appname__, __version__, __description__
from universe_bot.logger import logger
from universe_bot.plugin import register_all_plugins
from universe_bot.backend import available_backends


def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('--version', '-V', action='store_true', default=False,
                            help='print version')
        parser.add_argument('--debug', '-d', action='store_true', default=False,
                            help='debug mode')
        arguments = parser.parse_args()
        initialize(arguments.debug)
        application(arguments)
    except BaseException as e:
        if e.__class__.__name__ != 'SystemExit':
            logger().error(str(e.__class__.__name__) + ': ' + str(e))
        elif e.code != 0:
            logger().warning(str(e.__class__.__name__) + ': ' + str(e))

def application(args):
    if args.version:
        print(__appname__ + ' ' + __version__)
        print(__description__)
        sys.exit(0)
    register_all_plugins()
    # print(available_backends)
    # raise NotImplementedError('not implemented')

if __name__ == "__main__":
        main()
