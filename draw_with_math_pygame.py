import pygame
import pygame.gfxdraw

pygame.init()

# Set width and height of our screen we'll make next
screenWidth = 1000
screenHeight = 1000 

# create a screen to draw to with screenWidth and screenHeight
screen = pygame.display.set_mode((screenWidth, screenHeight)) 

white = (255,255,255) 
black = (0,0,0) 
 

running = True
while running: 
    screen.fill(black) 

    startX = screenWidth // 2
    startY = screenHeight // 2
    # Draw a single white pixel in the middle of the screen
    
    pygame.gfxdraw.pixel(screen, startX,startY, white) 
    i = startX
    for i in range(500 , 520):
        x = i
        y = -1*(i - 500)*(i - 500)
        y=y+500
        pygame.gfxdraw.pixel(screen,x,y, white)  


        
    
    for event in pygame.event.get():
        # if you try to quit, let's leave this loop
        if event.type == pygame.QUIT: 
            running = False # lets loop finish 

    # this is how we update the screen we've been drawing on.
    pygame.display.flip() 


