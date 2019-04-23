import pygame as py  
import element

# define constants  
WIDTH = 800  
HEIGHT = 600  
FPS = 30  

# define colors  
BLACK = (0 , 0 , 0)  
GREEN = (0 , 255 , 0) 
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# initialize pygame and create screen  
py.init()  
screen = py.display.set_mode((WIDTH , HEIGHT))  
# for setting FPS  
clock = py.time.Clock()  

rot = 0  
rot_speed = 2  

r = element.Rect(py, (100, 100),BLACK, GREEN, (WIDTH/2, HEIGHT/2), r, rot_speed)

running = True  
while running:  
    # set FPS  
    clock.tick(FPS)  
    # clear the screen every time before drawing new objects  
    screen.fill(BLACK)  
    # check for the exit  
    for event in py.event.get():  
        if event.type == py.QUIT:  
            running = False  

    r.show(py, screen)

py.quit()  



# import pygame

# game = True
# #DIMENSIONS
# WIDTH = 800
# HEIGHT = 600

# #COLORS
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)
# WHITE = (255, 255, 255)
# BLUE = (0, 0, 255)
# GREEN = (0, 255 ,0)

# #INIZIALATE GAME 
# pygame.init()
# gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
# clock = pygame.time.Clock()

# #GAME LOGICS
# while game:
#     for event in pygame.event.get(): 
#         if event.type == pygame.QUIT:
#             game = False



   
#     #DRAWING THINGS
#     gameDisplay.fill(WHITE)
#     pygame.draw.rect(gameDisplay, RED, (WIDTH/2, HEIGHT/2, 60, 40))


#     pygame.display.update()
#     clock.tick(60)

# pygame.quit()
# quit()
