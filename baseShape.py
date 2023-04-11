'''
Implement an abstract base class "Shape"
'''
# we need a tool to do this 
from abc import ABC

class Shape(ABC):
    def __init__(self, x = 0, y = 0):
        # coordinates x, y
        self.x = x
        self.y = y

        # pygame.rect()
        
    def getSize():
        pass
    