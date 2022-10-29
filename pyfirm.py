from email import iterators
from pyfirmata import Arduino, util

import time


board = Arduino('COM4')


iterator = util.Iterator(board)
iterator.start()


valve = board.get_pin('d:12:o')

time.sleep(1.0)

valve.write(1.0)

board.exit()


