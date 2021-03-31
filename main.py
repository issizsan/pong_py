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
pspeed = 7

mv1_up = False 
mv1_down = False
mv2_up = False
mv2_down = False 

player1 = pygame.Rect(10, ((height/2)-60), 12, 100)
player2 = pygame.Rect(width-22, ((height/2)-60), 12, 100)
ball = pygame.Rect(halfwidth, halfheight, 25, 25)
        
while True:
    screen.fill(black)
    ball.x += bspeed_x
    ball.y += bspeed_y

    if mv1_down:
        player1.y += pspeed
    elif mv1_up:
        player1.y -= pspeed
    
    elif mv2_down:
        player2.y += pspeed
    elif mv2_up:
        player2.y -= pspeed

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                mv1_down = True
            if event.key == pygame.K_w:
                mv1_up = True
            
            if event.key == pygame.K_DOWN:
                mv2_down = True
            if event.key == pygame.K_UP:
                mv2_up = True
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                mv1_down = False  
            if event.key == pygame.K_w:
                mv1_up = False  
            
            if event.key == pygame.K_DOWN:
                mv2_down = False  
            if event.key == pygame.K_UP:
                mv2_up = False  


    if ball.left < 0 or ball.right > width:
        bspeed_x *= -1
    if ball.top < 0 or ball.bottom > height:
        bspeed_y *= -1
    
    if ball.colliderect(player1):
        bspeed_x *= -1
    if ball.colliderect(player2):
        bspeed_x *= -1

    if player1.top < 0:
        mv1_up = False
    if player2.top < 0:
        mv2_up = False
    
    if player1.bottom > height:
        mv1_down = False
    if player2.bottom > height:
        mv2_down = False
    
    draw()
    pygame.display.update()
    fpsClock.tick(FPS)
