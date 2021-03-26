import sys, pygame
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0,0,0
white = (255, 255, 255)

screen = pygame.display.set_mode(size)  

"""
ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()
"""

pygame.draw.rect(screen, white, (10, ((240/2)-30), 10, 60))
pygame.draw.circle(screen, white, (320/2, 240/2), 10)
pygame.draw.rect(screen, white, (320-20, ((240/2)-30), 10, 60))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    """ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    
    screen.fill(black)
    screen.blit(ball, ballrect)
    """
    pygame.display.flip()
