#Nico Gonnella
#Ball driver
#Object oriented was the only way I could find to easily add balls, so I figured I would practice it.
#I did use a lot of the example code from the past ball exercise, but I really tried to write it by myself.
from graphics import *
import random

class Ball:
    
    def __init__(self, radius):
        self.radius = radius
        self.circle = Circle(Point(400,250), self.radius)
        self.circle.setFill("black")
        self.x_speed = 0
        self.y_speed = 0
    
    def change_color(self):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        color = color_rgb(r,g,b)
        self.circle.setFill(color)
        
    def y_center (self):
        return self.circle.getCenter().getY()
    
    def x_center (self):
        return self.circle.getCenter().getX()
        
    def right_side (self):
        return self.circle.getCenter().getX() + self.radius
    
    def left_side (self):
        return self.circle.getCenter().getX() - self.radius
    
    def top (self):
        return self.circle.getCenter().getY() + self.radius
    
    def bottom (self):
        return self.circle.getCenter().getY() - self.radius
    
    def move (self):
        self.circle.move(self.x_speed, self.y_speed)
    
    def draw (self, win):
        self.circle.draw(win)
    
    
    