""" ghost.py

Contains the Ghost class

"""

import random
from pose import Direction, Pose
from agent import Agent


class Ghost(Agent):
    """ Class to represent the Ghost agents """
    
    def __init__(self, world, pose, direction=Direction.RIGHT):
        super().__init__(world, pose, direction)        
        self.start_pose = pose              
        
        
    def find_next_heading(self):
        """Sets the direction to ghost should head in """
        if self.visible or (self.pose == self.start_pose):                 
            self.visible = True # when ghost reaches the start pose, it needs to be made visible again  
            
            # The ghost trys to head towards a pacman that is within line-of-sight           
            self.direction = self.pacman_direction()
            
            # If the Ghost has not spotted pacman, it picks a random direction
            if not self.direction:                  
                self.direction = self.select_random_heading()                           
        else: 
            # Ghost returning to start location after having eaten a pacman.
            #  currently, the Ghost walks through walls to return to the start.
            self.direction = self.location_heading(self.start_pose)        
                        
            
    def pacman_direction(self):
        """ Return the direction of a pacman if a pacman is within the ghost's line-of-sight.
            Otherwise returns None.
        """
        for pacman in self.world.get_pacmen():
            # If the pacman is horizontally or vertically aligned to the ghost,        
            #    check if a wall is blocking the ghost's line-of-sight.
            if pacman.get_pose().x == self.pose.x or pacman.get_pose().y == self.pose.y:
                x = self.pose.x
                y = self.pose.y
                spotted = True
                while x != pacman.get_pose().x or y != pacman.get_pose().y:
                    if not self.world.is_xy_traversable(x, y):
                        # There is a wall in the way, so the ghost cannot see pacman
                        spotted = False
                        break # break out while loop
                        
                    # move the location being checked along by 1.
                    if x < pacman.get_pose().x:
                        x = x + 1
                    elif x > pacman.get_pose().x:
                        x = x - 1
                    elif y < pacman.get_pose().y:
                        y = y + 1
                    elif y > pacman.get_pose().y:
                        y = y - 1
                        
                if spotted: # spotted pacman, so head towards pacman
                    return self.location_heading(pacman.get_pose())
        # no pacmen can be seen
        return None


    def location_heading(self, location):
        """ returns the direction this agent has to travel in to reach the provided location """
        next_direction = None
        if location.x > self.pose.x:
            next_direction = Direction.RIGHT
        elif location.x < self.pose.x:
            next_direction = Direction.LEFT
        elif location.y > self.pose.y:
            next_direction = Direction.DOWN
        elif location.y < self.pose.y:
            next_direction = Direction.UP
        
        return next_direction    

    
    def eat(self):
        """ if the ghost is visible and there are pacmen at the same location, 
            the ghost feeds on the pacmen.
        """
        if self.visible:
            pacmen = self.world.get_pacmen_at_loc(self.pose)
            for pacman in pacmen:
                if (pacman.is_visible()):
                    pacman.captured()
                    self.visible = False
                    self.amount_eaten = self.amount_eaten + 1
       
    # End of Ghost class
#=====================================
