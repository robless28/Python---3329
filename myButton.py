import pygame

class Button():
    def __init__(self,WINDOW,x,y,width,height,default, hover, clicked):
        self.WINDOW=WINDOW
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.BUT=pygame.Rect(x, y, width, height)
        self.state='default'
        self.default=default
        self.hover=hover
        self.clicked=clicked
        
    def draw(self):
        if self.state=='default':
            pygame.draw.rect(self.WINDOW,self.default,self.BUT)
        elif self.state=='hover':
            pygame.draw.rect(self.WINDOW,self.hover,self.BUT)
        elif self.state=='clicked':
            pygame.draw.rect(self.WINDOW,self.clicked,self.BUT)

    def eventResponse(self, eventObject):
     if eventObject.type == pygame.MOUSEMOTION or eventObject.type == pygame.MOUSEBUTTONDOWN or eventObject.type == pygame.MOUSEBUTTONUP:
        if self.BUT.collidepoint(eventObject.pos):
            if eventObject.type ==pygame.MOUSEMOTION:
                self.state='hover'
            elif eventObject.type == pygame.MOUSEBUTTONDOWN:
                self.state='clicked'
            elif eventObject.type == pygame.MOUSEBUTTONUP:
                self.state='hover'
     else:
         self.state='default'