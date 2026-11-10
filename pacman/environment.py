""" environment.py

    Controls what is displayed to the user.
"""

try:  # import as appropriate for 2.x vs. 3.x
   import tkinter as tk
   import tkinter.font as tkFont
except:
   import Tkinter as tk
   import Tkinter.font as tkFont
   
import random

import config
from world import World
from pose import Direction, Pose

class Display(tk.Tk):
    def __init__(self, game, world, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.canvas = tk.Canvas(self, width=1500, height=800, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")
        self.title("CMP2020 Pacman")
        
        self.world = world        
        
        self.cellwidth = 35
        self.cellheight = 35
        
        self.grid_offset_x = 150
        self.grid_offset_y = 50

        self.rect = {}
        self.oval = {}
        
        self.__draw_grid(self.world.walls)


    def update_display(self):
        """Updates the GUI with the updated locations of pacmen, ghosts and pellets, 
           and the updated scores and lives.
        """
        # delete pacmen, ghosts and pellets
        self.canvas.delete('agent') 
        
        # draw each pacman
        for pacman in self.world.get_pacmen():
            self.__draw_pacman(pacman.get_pose().x, pacman.get_pose().y, pacman.get_direction(), pacman.is_visible())              
        
        # draw each ghost
        for ghost in self.world.get_ghosts():
            self.__draw_ghost(ghost.get_pose().x, ghost.get_pose().y, ghost.is_visible())
            
        # draw each pellet
        for pellet in self.world.get_pellets():
            self.__draw_pellet(pellet.x, pellet.y)  

        self.__show_scores()


    def __draw_grid(self, walls):        
        for column in range(config.NUMBER_OF_COLUMNS):
            for row in range(config.NUMBER_OF_ROWS):
                x1, y1, x2, y2 = self.__rectangle_coordinates(column, row)
                if Pose(column, row) in walls:
                    self.rect[column, row] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="gray5", tags="wall_rect")
                else:                    
                    self.rect[column, row] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="ghost white", tags="empty_rect", outline='gray40', width=2)
   
        
    def __draw_pacman(self, col, row, direction, visible):        
        x1, y1, x2, y2 = self.__rectangle_coordinates(col, row)
        start = 15 + (direction * 90) # the starting degree for the oval: 15 for right; 105 for up; 195 for left and 285 for down
        if visible: # draw yellow pacman:
            self.oval[row,col] = self.canvas.create_arc(x1+2,y1+2,x2-2,y2-2, start=start, extent=325, fill="yellow", tags=("pacman", "agent"), width=5)
        else: # draw white pacman:
            self.oval[row,col] = self.canvas.create_arc(x1+2,y1+2,x2-2,y2-2, start=start, extent=325, fill="ghost white", tags=("pacman", "agent"), width=3)

        
    def __draw_ghost(self, col, row, visible):
        """
        Draws a ghost shape on the given canvas.
        
        Parameters:
            col, row (int): The grid location of the ghost.
            visible (str): False is the ghost has just captuered a pacman.
        """
        if visible:
            colour = "blue"
        else:
            colour = "ghost white" 
        
        x1, y1, x2, y2 = self.__rectangle_coordinates(col, row)
        # make ghost a little narrower than the grid square
        x = x1 + 4
        y = y1 + 3
        width = x2-x1 - 8
        height = y2-y1 - 6
        
        # The Ghost head is an arc
        self.canvas.create_arc(x, y, x + width, y + height, start=355, extent=190, fill=colour, outline=colour, tags=("ghost", "agent"))

        # Create the wavy bottom using a polygon
        wave_count = 6
        points = []
        for i in range(wave_count + 1):
            px = x + i * (width / wave_count)
            py = y + (height*0.65) + (10 if i % 2 == 0 else 5)  # alternating wave heights
            points.extend([px, py])
        # Close polygon by adding top corners
        points.extend([x + width, y + (height*0.5), x, y + (height*0.5)])
        self.canvas.create_polygon(points, fill=colour, outline=colour, tags=("ghost", "agent"))

        # The eyes are ovals
        eye_radius = width * 0.08
        eye_y = y + height * 0.4
        left_eye_x = x + width * 0.35
        right_eye_x = x + width * 0.65
        self.canvas.create_oval(left_eye_x - eye_radius, eye_y - eye_radius,
                           left_eye_x + eye_radius, eye_y + eye_radius, fill="black", tags=("ghost", "agent"))
        self.canvas.create_oval(right_eye_x - eye_radius, eye_y - eye_radius,
                           right_eye_x + eye_radius, eye_y + eye_radius, fill="black", tags=("ghost", "agent"))
    
    
    def __draw_pellet(self, col, row):
        x1, y1, x2, y2 = self.__rectangle_coordinates(col, row)
        # make the oval shape smaller than the grid square:
        x1 += self.cellwidth / 4
        y1 += self.cellheight / 4
        x2 -= self.cellwidth / 4
        y2 -= self.cellheight / 4
        # draw the oval
        self.oval[col,row] = self.canvas.create_oval(x1+2,y1+2,x2-2,y2-2, fill="dark green", tags=("pellet", "agent"), width=2)

        
    def __show_scores(self):
        self.canvas.delete('scores')
        
        # show the scores for each of the pacmen:
        self.canvas.create_text(65, 50, text="Scores", tags="scores", font=tkFont.Font(size=26, weight='bold'))
        for index, pacman in enumerate(self.world.get_pacmen()):
            self.canvas.create_text(65, 90+(25*index), text="Player "+ str(index) + ": " + str(pacman.amount_eaten), tags="scores", font=tkFont.Font(size=16))
            
        # show the number of remaining lives for each of the pacmen.
        self.canvas.create_text(65, 250, text="Lives", tags="scores", font=tkFont.Font(size=26, weight='bold'))
        for index, pacman in enumerate(self.world.get_pacmen()):
            self.canvas.create_text(65, 290+(25*index), text="Player "+ str(index) + ": " + str(pacman.lives), tags="scores", font=tkFont.Font(size=16))
        
        

    def __rectangle_coordinates(self, col, row):
        """ Translates the grid x,y to coordinates on the canvas. """
        x1 = (col*self.cellwidth) + self.grid_offset_x
        y1 = (row * self.cellheight) + self.grid_offset_y
        x2 = x1 + self.cellwidth
        y2 = y1 + self.cellheight
        return x1, y1, x2, y2

# End of class     
#================================================================
