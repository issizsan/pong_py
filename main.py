import sys, pygame, random
from pygame.locals import *

FPS = 30
fpsClock = pygame.time.Clock()

pygame.init()

size = width, height = 640, 480
halfwidth = width / 2
halfheight = height / 2

speed = [2, 2]
black = 0,0,0
white = (255, 255, 255)

screen = pygame.display.set_mode(size)  

def draw():
    pygame.draw.rect(screen, white, player2)
    pygame.draw.rect(screen, white, player1)
    pygame.draw.rect(screen, white, ball, border_radius=20)

bspeed_x = 7
bspeed_y = 7

movement = 'up'

player1 = pygame.Rect(10, ((height/2)-60), 12, 100)
player2 = pygame.Rect(width-22, ((height/2)-60), 12, 100)
ball = pygame.Rect(halfwidth, halfheight, 25, 25)
        
while True:
    screen.fill(black)
    ball.x += bspeed_x
    ball.y += bspeed_y

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_DOWN:
                player1.y -= 5

    if ball.left < 0 or ball.right > width:
        bspeed_x *= -1
    if ball.top < 0 or ball.bottom > height:
        bspeed_y *= -1
    
    if ball.colliderect(player1):
        bspeed_x *= -1
    if ball.colliderect(player2):
        bspeed_x *= -1

    draw()
    pygame.display.update()
    fpsClock.tick(FPS)
