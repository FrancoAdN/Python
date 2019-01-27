import pygame
import func as f
import classFile as cf

#colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

dim=(400,400)
#class Ball parameters = (self, r, start, color, speed)
circle = cf.Ball(10,[200,400],red,[5,5])
#class Rect parameters = (self,len,start,color,speed,direction)
rect = cf.Rect(20,[dim[0]/2-10,dim[1]/2],black,1,'r')

pygame.init()
gameDisplay = pygame.display.set_mode(dim)
clock = pygame.time.Clock()

#game loop
game = True
while game:
    #event's logic
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game = False
            if event.key == pygame.K_RIGHT:
                rect.direction = 'r'
            elif event.key == pygame.K_LEFT:
                rect.direction = 'l'
            elif event.key == pygame.K_UP:
                rect.direction = 'u'
            elif event.key == pygame.K_DOWN:
                rect.direction = 'd'


    
    #COLISION LOGIC
    #circle w/walls colision    
    if circle.start[0] <= circle.r:
        circle.direction = [circle.speed[0],-circle.speed[1]]
    elif circle.start[1] <= circle.r:
        circle.direction = [circle.speed[0],circle.speed[1]]
    elif circle.start[0] >= dim[0] - circle.r:
        circle.direction = [-circle.speed[0],circle.speed[1]]
    elif circle.start[1] >= dim[1] - circle.r:
        circle.direction = [-circle.speed[0],-circle.speed[1]]
    #rect w/walls colision
    if (rect.start[0] + rect.speed > dim[0] - rect.len[0]) or (rect.start[0] - rect.speed < 0) or (rect.start[1] - rect.speed < 0) or (rect.start[1] + rect.speed > dim[1] - rect.len[0]):
        game = False
    #rect w/circle
    if f.d([rect.start[0] + rect.len[0]/2, rect.start[1] + rect.len[1]/2],circle.start) <= 20:
        game = False
    
    

    
    circle.move()
    rect.move()  


    #drawing things on display
    gameDisplay.fill(white)
    pygame.draw.circle(gameDisplay,circle.color,circle.start,circle.r)
    pygame.draw.rect(gameDisplay, rect.color, (rect.start,rect.len))
     

    #update display and tick
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
