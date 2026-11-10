""" world.py

Contains the World class

"""
import random

import config
import maps
from pose import Pose, Direction

class World:
    """ Holds the state of the world: the walls, the pacmen and the ghosts"""
    
    def __init__(self):        
        self.max_x = config.NUMBER_OF_COLUMNS - 1
        self.max_y = config.NUMBER_OF_ROWS - 1         
        
        self.walls, self.pellets = maps.parse_map(config.LEVEL)        

        self.pacmen = []
        self.ghosts = []
    
    #------------ 
        
    def remove_pellet_at_location(self, pose):
        """ returns true if a pellet was found at the provided pose """
        if pose in self.pellets:
            self.pellets.remove(pose)
            return True
        return False
        
    
    def get_pacmen_at_loc(self, pose):
        """ returns the pacmen at the given pose or an empty list """
        pacmen_at_loc = []
        for pacman in self.pacmen:
            if pacman.pose == pose:
                pacmen_at_loc.append(pacman)
        return pacmen_at_loc
    
    
    def any_pacmen_alive(self):
        """ returns true if any pacmen are still alive """
        for pacman in self.pacmen:
            if pacman.is_alive():
                return True
        return False
        
    #------------ 
    
    def get_actions(self, pose):
        """ returns the Directions that and agent can move in from the provided location (Pose object) """
        possible_moves = []
        
        if self.is_xy_traversable(pose.x + 1, pose.y):
            possible_moves.append( Direction.RIGHT )
             
        if self.is_xy_traversable(pose.x - 1, pose.y):
            possible_moves.append( Direction.LEFT )
        
        if self.is_xy_traversable(pose.x, pose.y + 1):
            possible_moves.append( Direction.DOWN )
        
        if self.is_xy_traversable(pose.x, pose.y - 1):
            possible_moves.append( Direction.UP )
            
        return possible_moves  

    #------------ 
    
    def get_successor_state(self, location, action, agent_invisible=False):
        """ returns the location reached when the provided action (Direction) is executed """
        pose = Pose(location.x, location.y)
        if action == Direction.RIGHT :
            pose.x = pose.x + 1             
        elif action == Direction.LEFT:
            pose.x = pose.x - 1 
        elif action == Direction.DOWN:
            pose.y = pose.y + 1 
        elif action == Direction.UP:
            pose.y = pose.y - 1 
                  
        if self.is_traversable(pose) or agent_invisible:
            return pose
        else:
            return location       
    
    #------------ 
    
    def is_traversable(self, pose):
        """ can the agent enter the provided Pose? """
        return ( (pose not in self.walls) 
                   and (pose.x >= 0) and (pose.y >= 0) 
                    and (pose.x <= self.max_x) and (pose.y <= self.max_y) )
     
    #------------    
    
    def is_xy_traversable(self, x, y):
        """ can the agent enter the provided x,y position? """
        return self.is_traversable(Pose(x, y))       
    
    #------------ 
    
    def get_random_unoccupied_pose(self):
        """ Returns a random empty location  """
        x = random.randint(0, self.max_x)    
        y = random.randint(0, self.max_y)
        while not self.is_xy_traversable(x, y):
            x = random.randint(0, self.max_x)    
            y = random.randint(0, self.max_y)
        return Pose(x, y)
        
    #------------ 
    
    def get_random_unoccupied_lr_edge_pose(self):
        """ Returns a random empty pose on either the left or right edge of the grid.
            This is used to select a starting location for each pacman.
        """
        x = random.choice([0, self.max_x])    
        y = random.randint(0, self.max_y)
        while not self.is_xy_traversable(x, y):
            x = random.choice([0, self.max_x])   
            y = random.randint(0, self.max_y)
        return Pose(x, y)
    #------------ 
    
    def get_random_unoccupied_tb_edge_pose(self):
        """ Returns a random empty pose on either the top or bottom edge of the grid
            This is used to select a starting location for each ghost.
        """
        x = random.randint(0, self.max_x)    
        y = random.choice([0, self.max_y])
        while not self.is_xy_traversable(x, y):
            x = random.randint(0, self.max_x)    
            y = random.choice([0, self.max_y])
        return Pose(x, y)
        
    #-------
    # getters and setters
    
    def add_pacman(self, pacman):
        self.pacmen.append(pacman)
        
    def add_pellet(self, pellet):
        self.pellets.append(pellet)
            
    def add_ghost(self, ghost):
        self.ghosts.append(ghost)
    
    def get_pacmen(self):
        return self.pacmen        
        
    def get_pellets(self):
        return self.pellets
        
    def get_ghosts(self):
        return self.ghosts
        
    def get_all_agents(self):
        return self.pacmen + self.ghosts  
    #-------
#=========================
