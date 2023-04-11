# Setup 
import pygame
# Initialize pygame
pygame.init()
# Display
gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Display')
#Clock
clock = pygame.time.Clock()
#Load an image
gameDisplay.fill((255, 255, 255))
myimage = pygame.image.load('descarga.png')

#gameDisplay.blit(myimage, (50,50))
# Main Application loop
while True:
    #Listen for events
    for event in pygame.event.get():
      print(event)
      
    #event = pygame.event()[0]
    # Create an exit event
      if event.type == pygame.WINDOWCLOSE:
        pygame.quit()
    
    gameDisplay.blit(myimage, (50,50))
    pygame.display.update()

    clock.tick(10)