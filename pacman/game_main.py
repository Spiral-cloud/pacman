""" game_main.py
#
# Contains the Game class and the code to start-up the applications
#
# Written by: Helen Harman
"""

import random

from pose import Direction
from world import World
from pacman import Pacman
from ghost import Ghost
from environment import Display
import config

class Game():
    """ Class to control the game """
    
    def __init__(self):
        
        self.world = World()
        self.app = Display(self, self.world)
        
        # setup pacmen
        for mode in config.PACMEN_MODES:
            pacman = Pacman(self.world, self.world.get_random_unoccupied_lr_edge_pose(), Direction.RIGHT, mode)
            self.world.add_pacman(pacman)
        
        # setup pellets
        for i in range(config.NUMBER_OF_PELLETS):
            pellet = self.world.get_random_unoccupied_pose()
            self.world.add_pellet(pellet)
        
        # setup ghosts
        for i in range(config.NUMBER_OF_GHOSTS):
            ghost = Ghost(self.world, self.world.get_random_unoccupied_tb_edge_pose())
            self.world.add_ghost(ghost)
        
        # show initial world state
        self.app.update_display()
           
        self.game_over = False   
        
    
    def start_game(self):
        """ Calls play() for the first time and launches the GUI """
        self.app.after(config.LOOP_DELAY, lambda: self.play())
        self.app.mainloop()
        
        
    def play(self):
        """ The main control loop for the game. This method is recursively called. """            
        for agent in self.world.get_all_agents():              
            agent.eat() # This eat has been added so that pacman/ghost leaping over each other results in a life being lost.
            agent.find_next_heading()
            agent.move_forward()
            agent.eat() # Pacmen eat pellets. Ghosts eat pacmen.
            
        self.app.update_display()
        
        if (self.is_game_over()):
            print("Game over!")
            print("Number of pacmen each ghost ate:")
            for index, ghost in enumerate(self.world.get_ghosts()):
                print("Ghost ", index, ": ", ghost.amount_eaten)
        else: # recursively call play() after a delay
            self.app.after(config.LOOP_DELAY, lambda: self.play())
 
 
    def is_game_over(self):
        """ The game ends when there are no pellets left or there are no living Pacmen """
        return ( (not self.world.get_pellets()) or (not self.world.any_pacmen_alive()) )
 
#================
# MAIN 

if __name__ == "__main__":
    game = Game()
    game.start_game()
    
# EOF
#============================================
