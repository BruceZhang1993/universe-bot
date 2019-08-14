import argparse
import sys
import os
from universe_bot import initialize
from universe_bot.logger import logger
from universe_bot.app import application


def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('--version', '-V', action='store_true', default=False,
                            help='print version')
        parser.add_argument('--debug', '-d', action='store_true', default=False,
                            help='debug mode')
        parser.add_argument('--conf', '-c', action='store', default=None,
                            help='config file')
        arguments = parser.parse_args()
        initialize(arguments.debug)
        application(arguments)
    except BaseException as e:
        if e.__class__.__name__ != 'SystemExit':
            logger().error(str(e.__class__.__name__) + ': ' + str(e))
        elif e.code != 0:
            logger().warning(str(e.__class__.__name__) + ': ' + str(e))

if __name__ == "__main__":
        main()
