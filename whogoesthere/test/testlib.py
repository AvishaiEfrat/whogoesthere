import logging
import time

def stall(duration, reason):
    logging.info(f'stalling {duration} seconds for: {reason}')
    time.sleep(duration)
