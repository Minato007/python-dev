import pygame
import random

state = 'gamestart'

class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.dy = 0
        self.score = 0


class Ball:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.dx = 0
        self.dy = 0
        while self.dx == 0 or self.dy == 0:
            self.dx = random.randint(-3, 3)
            self.dy = random.randint(-3, 3)
        self.img = pygame.image.load('ball.png')
        self.img = pygame.transform.scale(self.img, (self.size, self.size))
        self.move = False


size = (540, 500)

player1 = Player(5, 100, 20, 100)
player2 = Player(size[0]-5-20, 100, 20, 100)

balls = []
ball = Ball(size[0]/2-20, size[1]/2-20, 40)
balls.append(ball)

pygame.init()
pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 30)
myfont1 = pygame.font.SysFont('Calibri', 65, True, False)
text_game_over = myfont1.render("Game Over", True, (255,0,0))
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
done = False

c = 0

clock = pygame.time.Clock()
counter = 5
text = '5'
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)

while not done:

    for event in pygame.event.get():

        if event.type == pygame.USEREVENT:
            counter -= 1
            if counter > 0:
                text = str(counter)
            else:
                text = 'new ball'
                ball = Ball(size[0]/2-20, size[1]/2-20, 40)
                ball.move = True
                balls.append(ball)
                counter = 5
                text = '5'

        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ball.move = True
            if event.key == pygame.K_s:
                player1.dy = 5
            if event.key == pygame.K_w:
                player1.dy = -5
            if event.key == pygame.K_DOWN:
                player2.dy = 5
            if event.key == pygame.K_UP:
                player2.dy = -5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                player1.dy = 0
            if event.key == pygame.K_w:
                player1.dy = 0
            if event.key == pygame.K_DOWN:
                player2.dy = 0
            if event.key == pygame.K_UP:
                player2.dy = 0

    if state == "gamestart":

        player1.y += player1.dy
        player2.y += player2.dy

        if player1.y < 1:
            player1.y = 1
        if player2.y < 1:
            player2.y = 1
        if player1.y > size[1] - 1 - player1.height:
            player1.y = size[1] - 1 - player1.height
        if player2.y > size[1] - 1 - player2.height:
            player2.y = size[1] - 1 - player2.height

        for ball in balls:
            if ball.move:
                ball.x += ball.dx
                ball.y += ball.dy

        # Bounce
        for ball in balls:
            if ball.x > size[0] - ball.size - player2.width:
                if (ball.y + ball.size/2 > player2.y) and (ball.y + ball.size/2 < player2.y + player2.height):
                    ball.dx = -abs(ball.dx)
                    ball.dx = ball.dx * 1.1
                    ball.dy = ball.dy * 1.1
                else:
                    # ball = Ball(size[0] / 2 - 20, size[1] / 2 - 20, 40)
                    # ball.move = True
                    balls.remove(ball)
                    player1.score += 1
                    c = 0

        for ball in balls:
            if ball.y > size[1] - ball.size:
                ball.dy = -abs(ball.dy)

        for ball in balls:
            if ball.x < player1.x + player1.width:
                if (ball.y + ball.size/2 > player1.y) and (ball.y + ball.size/2 < player1.y + player1.height):
                    ball.dx = abs(ball.dx)
                    ball.dx = ball.dx * 1.1
                    ball.dy = ball.dy * 1.1
                else:
                    # ball = Ball(size[0] / 2 - 20, size[1] / 2 - 20, 40)
                    # ball.move = True
                    balls.remove(ball)
                    player2.score += 1
                    c = 0

        for ball in balls:
            if ball.y < 1:
                ball.dy = abs(ball.dy)

        c += 10
        if c > 255:
            c = 255

    if state == "gameOver":
        c = 255
    screen.fill((255,c,c))

    pygame.draw.rect(screen, (0, 128, 0), [
        player1.x, player1.y, player1.width, player1.height
    ], 0)

    pygame.draw.rect(screen, (0, 128, 0), [
        player2.x, player2.y, player2.width, player2.height
    ], 0)

    for ball in balls:
        screen.blit(ball.img, (ball.x, ball.y))

    text_surface = myfont.render(str(player1.score),False,(20,20,250))
    screen.blit(text_surface, (size[0]/3, 10))

    text_surface = myfont.render(str(player2.score),False,(20,20,250))
    screen.blit(text_surface, (size[0]*2/3, 10))

    screen.blit(font.render(text, True, (0, 0, 0)), (250, 10)) #вывод каунтера на экран

    if (player1.score == 3) or (player2.score == 3):
        state = 'gameOver'

    if state == 'gameOver':
        screen.blit(text_game_over, [10, 200])

    pygame.display.flip()
    clock.tick(80)

pygame.quit()
