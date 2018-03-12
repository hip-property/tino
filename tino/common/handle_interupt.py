import signal
import sys


# noinspection PyUnusedLocal
def signal_handler(signal, frame):
    print('Interrupted')
    sys.exit(0)


def handle_interrupt():
    signal.signal(signal.SIGINT, signal_handler)
