import signal
import sys
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from universe_bot import __appname__, __version__, __description__
from universe_bot.config import Config
from universe_bot.logger import logger
from universe_bot.connector import connection

STARTED_CONNECTIONS = []


def global_signal_handler(_, __):
    logger().info('Gracefully stopping all connections...')
    for conn in STARTED_CONNECTIONS:
        conn.stop()
    sys.exit(0)


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
    signal.signal(signal.SIGINT, global_signal_handler)
    with ThreadPoolExecutor(max_workers=os.cpu_count()) as pool:
        connections = Config().get('connections')
        task = [pool.submit(connection, name=c, c=connections[c]) for c in connections]
        for future in as_completed(task):
            future.result()
    raise NotImplementedError('not implemented')
