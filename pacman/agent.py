""" agent.py

Contains the Agent class

"""
from abc import ABC, abstractmethod
import random

class Agent(ABC):
    """ Class to represent the agents (e.g. Pacmen and Ghosts) within the world """    
    
    def __init__(self, world, pose, direction):
        self.world = world
        self.pose = pose
        
        self.direction = direction
        
        self.visible = True # Pacmen become invisble when they die. Ghost become invisible after eating a Pacman. 
        self.amount_eaten = 0 # Number of pellets or number of pacmen that have been eaten by this agent.
      
    @abstractmethod
    def find_next_heading(self):
        """ Sets self.direction to the direction the agent should move in"""
        pass

    @abstractmethod
    def eat(self):
        """ All agents need to eat but they eat different items """
        pass

    
    def select_random_heading(self):    
        """ returns a random traversable direction """    
        return random.choice(self.world.get_actions(self.pose))
    
    def move_forward(self):
        """ moves the agent forwards by one grid square 
            If the grid location contains a wall, the agent stays still.
        """   
        self.pose = self.world.get_successor_state(self.pose, self.direction, self.visible)     
 
    #--------
    # Getters and setters
    
    def get_pose(self):
        return self.pose
        
    def get_direction(self):
        return self.direction
    
    def is_visible(self):
        return self.visible
    #-------


    # End of Agent class
#=============================
