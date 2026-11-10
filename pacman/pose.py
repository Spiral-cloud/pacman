""" pose.py

 Contains the Pose class and the Direction enum

 Written by: Simon Parsons
 Modified by: Helen Harman
"""

import math
from enum import IntEnum

class Direction(IntEnum):
    RIGHT = 0,
    UP = 1,
    LEFT = 2,
    DOWN =3


class Pose():
    """ Class to represent the position of elements within the world """   
    
    def __init__(self, *args): 
        self.x = 0
        self.y = 0
        if len(args) > 1:
            self.x = args[0]
            self.y = args[1]        
        
    
    def distance_to(self, p): 
        """ returns the Euclidean distance between this pose 
                and the provided pose. 
        """
        return math.dist([self.x, self.y], [p.x, p.y])
        
    def print(self):
        print('[', self.x, ',', self.y, ']')        
    
    def __repr__(self):
        return f"<Pose x:{self.x} y:{self.y}>"
            
    def __str__(self):
        return f"[{self.x},{self.y}]"
        
    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Pose):
            return (self.x == other.x and self.y == other.y)
        return False

    # End of Pose class
#=======================
