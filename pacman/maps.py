""" maps.py

   Contans the the different Pacman maps and the method to translate this into a list of wall locations.

"""

import config
from pose import Pose 
 
pacman_maps = [
    # 25 columns, 10 rows:
    [   "#### ####       #### ####",
        "#                       #",
        "#  ####   #    #  ####  #",
        "#  ####   #    #  ####  #",
        "         ###  ###        ",
        "         ###  ###        ",
        "#  ####   #    #  ####  #",
        "#  ####   #    #  ####  #",
        "#                       #",
        "#### ####       #### ####"
    ],
    # 30 columns, 20 rows:
    [   "#########            #########",
        "#                            #",
        "   ####   #  ####  #   ####   ",
        "   ####   #  ####  #   ####   ",
        "#       ####      ####       #",
        "#                            #",
        "# #### ### ######## ### #### #",
        "# #### ### ######## ### #### #",
        "  ###   #    ####    #   ###  ",
        "  ###   #            #   ###  ",
        "  ###   #            #   ###  ",
        "  ###   #    ####    #   ###  ",
        "# #### ### ######## ### #### #",
        "# #### ### ######## ### #### #",
        "#                            #",
        "#       ####      ####       #",
        "   ####   #  ####  #   ####   ",
        "   ####   #  ####  #   ####   ",
        "#                            #",
        "#########            #########"
    ],
    # You can add more levels. When adding a level, also modify the if statement
    #       within config.py so that the correct sized grid is used.
    #
    # To fix the location of the pellets, change a space to a . within the map 
    #       (and set config.NUMBER_OF_PELLETS to 0 to prevent random pellets being created).
 ]


def parse_map(level):
    """
    Transforms the string map into a list of wall locations and pellet locations.
    
    Parameters:
        level (int): Used to index which of the maps to use.
 
    """
    pacman_map = pacman_maps[level]
   
    walls = []
    pellet = []
    
    for row_idex, row in enumerate(pacman_map):
        for col_idex, cell in enumerate(row):
            if cell == "#":  # "#" represents a wall
                walls.append(Pose(col_idex, row_idex))
            elif cell == ".": # "." represents a pellet
                pellet.append(Pose(col_idex, row_idex))
                
    return walls, pellet
                
                
 #=========================================   
