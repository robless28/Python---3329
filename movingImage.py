import pygame

from myButton import Button

pygame.init()

# display
window = pygame.display.set_mode((800, 600))

# create a button instance 
BUTTONONE = Button(window,100, 100, 100, 50,(128, 0, 0),(255, 0, 255),(255, 255, 0))
BUTTONTWO = Button(window,300, 100, 100, 50,(128, 0, 0),(255, 0, 255),(255, 255, 0))

TheButtons = [BUTTONONE,BUTTONTWO]

# clock
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        for activebuttons in TheButtons:
            activebuttons.eventResponse(event)

    window.fill((192, 192, 192))
    for activebuttons in TheButtons:
        activebuttons.draw()
            

    pygame.display.update()
    clock.tick(60)