import pygame
dHeight = 600
dWidth = 800

pygame.init()
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)


gameDisplay = pygame.display.set_mode((dWidth,dHeight))
pygame.display.set_caption('HOW U DOIN')
clock = pygame.time.Clock()

carImg = pygame.image.load('img/car.png')

def car(x,y):
    gameDisplay.blit(carImg,(x,y))


x = (dWidth / 3)
y = (dHeight / 2)
x_change = 0

crash = False

while  not crash:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crash = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            if event.key == pygame.K_RIGHT:
                x_change = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0

        #print(event)
    if (x + x_change) < dHeight and (x + x_change) > 0:
        x += x_change
        print(x)

    gameDisplay.fill(white)
    car(x,y)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
