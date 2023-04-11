# setup 
import pygame
# from myButton import aButton

# initialize pygame 
pygame.init()

# display 
gameDisplay = pygame.display.set_mode((800, 600))
# pygame.display.get_caption('this is a caption')

# clock 
clock = pygame.time.Clock()

# load an image 
gameDisplay.fill((255, 136, 34))
myImg = pygame.image.load('descarga.png')
  #gameDisp.blit(myImg, (100, 100))
myotherimage = pygame.image.load('cow.jpg')


#gameDisp.blip(myImg, (100, 100))

# main application loop 
while True: 
    # listen for event
    for event in pygame.event.get():        # print each item from list
        print(event)

    # if event.type == pygame.QUIT:
        # pygame.quit()
        # exit()
                                               # this is what the professor wrote on the board
    # try:
        # print(event.pos)
    # except:
        # pass

    # part 3 - create an exit event 
        gameDisplay.blit(myImg, (100, 100))
        if event == pygame.WINDOWCLOSE:
            pygame.quit()
    x = 0
    y = 0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        gameDisplay.blit(myotherimage, (50, 50))
    if keys[pygame.K_d]:
        gameDisplay.blit(myImg, (50, 50))
    if keys[pygame.K_s]:
        gameDisplay.blit(myotherimage, (50, 50))
    if keys[pygame.K_w]:
        gameDisplay.blit(myImg, (50, 50))


    
    pygame.display.update()
    clock.tick(10)