import pygame
import random

pygame.init()
pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 30)
size = (400, 500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
done = False
img = pygame.image.load('pacman.png') #<---------upload png
x = 100
y = 100
dx = 0
dy = 0
eaten = False
food_position_x = random.randrange(50, 351)
food_position_y = random.randrange(50, 451)
counter = 0;

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                dx = 4
            if event.key == pygame.K_LEFT:
                dx = -4
            if event.key == pygame.K_UP:
                dy = -4
            if event.key == pygame.K_DOWN:
                dy = 4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                dx = 0
            if event.key == pygame.K_LEFT:
                dx = 0
            if event.key == pygame.K_UP:
                dy = 0
            if event.key == pygame.K_DOWN:
                dy = 0

    #logic
    x = x + dx
    y = y + dy
    if (food_position_x-10<x+50<food_position_x+10) & (food_position_y-10<y+50<food_position_y+10):
        eaten = True
    #end of logic
    screen.fill((255, 255, 255))

    if not eaten:
        pygame.draw.rect(screen, (200, 100, 100), [food_position_x, food_position_y, 10, 10], 15)
    else:
        food_position_x = random.randrange(50, 351)
        food_position_y = random.randrange(50, 451)
        counter += 1
        eaten = False
        pygame.draw.rect(screen, (200, 100, 100), [food_position_x, food_position_y, 10, 10], 15)

    screen.blit(img, (x, y))
    textsurface = myfont.render(str(counter), False, (0, 0, 0))
    screen.blit(textsurface,(50, 50))
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
