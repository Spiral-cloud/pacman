""" pacman.py

Contains the Pacman class
"""

from config import Mode, MAX_LIVES
from agent import Agent


class Pacman(Agent):
    """ Class to represent the Pacman agent """
    
    def __init__(self, world, pose, direction, mode):
        super().__init__(world, pose, direction)
        
        self.mode = mode
        
        self.lives = MAX_LIVES 

    def find_next_heading(self):   
        """ Sets the direction the pacman should head in """
        if self.mode == Mode.RANDOM:   
            self.direction = self.select_random_heading()
            
        #elif self.mode == ...
        
        #----
        # YOUR CODE
        # Hint: 
        #    (1) if there is no plan, create a plan.
        #    (2) self.direction = the next step in the plan 
        #----    
    
    
    def eat(self):
        """ Pacman eats a pellet :) """
        if self.is_alive() and self.world.remove_pellet_at_location(self.pose):
            self.amount_eaten = self.amount_eaten + 1
    
    
    def captured(self):
        """ A ghost ate Pacman :(  """
        self.lives = self.lives - 1
        if self.lives <= 0:
            self.visible = False
    
    
    def is_alive(self):
        """ Returns true if pacman has lives remaining """
        return self.lives > 0
           
    # End of Pacman class
#=========================
