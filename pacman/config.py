""" config.py
 
"""

from enum import Enum

class Mode(Enum):
    RANDOM = 0,
     # Add more options here

LOOP_DELAY = 500 # reduce this to speed-up the game. (Is in milliseconds)

# The code we have provided, creates two pacmen. Both of them select RANDOM headings.
# The length of the PACMEN_MODES array determines how many pacmen are created (and the content controls what mode the pacmen are in).
# You will want to change this when evaluating your approaches.
PACMEN_MODES = [Mode.RANDOM, Mode.RANDOM] 

MAX_LIVES = 3

NUMBER_OF_PELLETS = 50

NUMBER_OF_GHOSTS = 7

LEVEL = 1 

# see map.py for the different levels. We have provided you with 2 levels (you can create more).
if LEVEL == 0:
    NUMBER_OF_COLUMNS = 25
    NUMBER_OF_ROWS = 10
elif LEVEL == 1:
    NUMBER_OF_COLUMNS = 30
    NUMBER_OF_ROWS = 20
else:
    NUMBER_OF_COLUMNS = 30
    NUMBER_OF_ROWS = 20
