import pygame
import func as f
'''dHeight = 400
dWidth = 400'''
dim=(400,400)

pygame.init()
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

speed = 5

gameDisplay = pygame.display.set_mode(dim)
clock = pygame.time.Clock()
circle = [200,400]
dir = [-speed,-speed]



crash = False
while  not crash:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crash = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                crash = True
    
    if f.d(circle,(0,dim[1]/2)) <= 10:
        dir = [speed,-speed]
    elif f.d(circle,(dim[0]/2,0)) <= 10:
        dir = [speed,speed]
    elif f.d(circle,(dim[0],dim[1]/2)) <= 10:
        dir = [-speed,speed]
    elif f.d(circle,(dim[0]/2,dim[1])) <= 10:
        dir = [-speed,-speed]


    circle[0] += dir[0]
    circle[1] += dir[1]    

    gameDisplay.fill(white)
    pygame.draw.circle(gameDisplay,red,circle,10)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
