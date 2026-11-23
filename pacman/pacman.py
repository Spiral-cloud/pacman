""" pacman.py

Contains the Pacman class
"""

from config import Mode, MAX_LIVES
from agent import Agent
from pose import Pose
from collections import deque
from heapq import heappush,heappop

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
        elif self.mode == Mode.Agent:
            if not self.plan:
                self.plan = self.Agent()
            if self.plan:
                self.direction = self.plan.pop(0)
            else:
                self.direction = self.select_random_heading()
        elif self.mode == Mode.DEPTH:
            self.plan = self.depth_first_search()
            if self.plan:
                self.direction = self.plan.pop(0)
            else:
                self.direction = self.select_random_heading()
            
        #elif self.mode == ...
        
        #----
        # YOUR CODE
        # Hint: 
        #    (1) if there is no plan, create a plan.
        #    (2) self.direction = the next step in the plan 
        #----    
    #Uniform cost search
    def Agent(self):
        start = (self.pose.x, self.pose.y)
        pellets = self.world.get_pellets
        for pellet in pellets():
            pellet_location = {(pellet.x, pellet.y) for pellet in self.world.get_pellets()}
        frontier = deque([start])
        visited = {start}
        previous = {start: None}
        while frontier:
            current = frontier.popleft()
            if current in  pellet_location:
                return self.direction_plan(
                    start,
                    current,
                    previous
                )
            x, y = current
            current_pose = Pose(x,y)
            for direction in self.world.get_actions(current_pose):
                next = self.world.get_successor_state(current_pose, direction)
                
                '''next = self.world.get_successor_state
                (
                    current_pose,
                    direction
                )'''
                next_location = (next.x, next.y)
                if next_location not in visited:
                    visited.add(next_location)
                    previous[next_location] = (current, direction)
                    frontier.append(next_location)
        return[]
    #Helper function for depth_first_search and uniform_cost_search
    def direction_plan(self, start, goal, previous):
        plan = []
        current = goal
        while current != start:
            parent, direction = previous[current]
            plan.append(direction)
            current = parent
        plan.reverse()
        return plan
    #Because every node is equal to one this has the same result as uniform cost search, breadth first search also would have the same result
    def depth_first_search(self):
         start = (self.pose.x, self.pose.y)
         pellets = self.world.get_pellets
         for pellet in pellets():
            pellet_location = {(pellet.x, pellet.y) for pellet in self.world.get_pellets()}
            stack = [start]
            visited = {start}
            previous = {start: None}
            while stack:
                current = stack.pop()
                if current in pellet_location:
                    return self.direction_plan(start, current,previous)
            x,y = current
            current_pose = Pose(x,y)
            for direction in self.world.get_actions(current_pose):
                successor = self.world.get_successor_state
                (
                    current_pose, direction
                )
                next_location = (successor.x, successor.y)
                if next_location not in visited:
                    visited.add(next_location)
                    previous[next_location] = (current, direction)
                    stack.append(next_location)
         return []
    def A_star_search(self):
        start = (self.pose.x, self.pose.y)
        pellets = self.world.get_pellets
        for pellet in pellets():
            pellet_location = {(pellet.x, pellet.y) for pellet in self.world.get_pellets()}
        if not pellet_location:
            return[]

            
    
    
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
