import pygame
import sys
import random
pygame.init()
WHITE=(225,225,225)
GREY=(200,200,200)
BLACK=(0,0,0)
RED=(255,0,0)
BLUE=(0,0,255)
SEAGREEN = (0, 255, 182)
GREEN=(0,225,0)

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Tycoon")
money=0
timer = 0
upgrades = 0
moneyrate=upgrades+1
price = 0
hasball=0
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

#ball
ball = pygame.Rect(390, 300, 15, 15)
ball_dx = 4
ball_dy = -4

#rocket
rx=400
dirr = 1
#blok
bx= 350
by=280


while True:
    clock.tick(60)  # 60 FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit("Tycoon was closed by User")
    timer += 1
    if timer % 75 == 0:
        money += moneyrate
    price = (upgrades*20)+10

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        if money >= price:
            money -= price
            moneyrate += 1
            upgrades += 1
    #the ball's physics
    ball.x += ball_dx
    ball.y += ball_dy
    if ball.left <= 0 or ball.right >= 800-20:
        ball_dx *= -1
    if ball.top <= 0 or ball.bottom >= 580:
        ball_dy *= -1
    #the rocket's physics
    rx += dirr
    if ball.left <= 20 or ball.right >= 780:
        dirr *= -1
    

    if upgrades > 0:
        #cubit
        pygame.draw.rect(screen, SEAGREEN, (400, 500, 50, 50))
        pygame.draw.rect(screen, BLACK, (400, 500, 20, 30))
        pygame.draw.rect(screen, BLACK, (430, 500, 20, 30))
    if upgrades > 2:
        #rocket
        pygame.draw.rect(screen, RED, (rx-10, 350, 70, 20))
        pygame.draw.rect(screen, WHITE, (rx, 300, 50, 70))
        pygame.draw.rect(screen, WHITE, (rx+15, 280, 20, 70))

    if upgrades > 4:
        #ball
        pygame.draw.ellipse(screen, (255, 255, 255), ball)
    if upgrades > 6:
        #block
        pygame.draw.rect(screen, GREEN, (bx,by,100,40))
        if timer % 100==0:
            bx=random.randint(0,700)
            by=random.randint(0,560)

    Moneytext = font.render(f"Money: {money}", True, BLACK)
    stats = font.render(f"Upgrades: {upgrades}", True, BLACK)
    screen.blit(Moneytext, (10, 10))
    buy = font.render(f"Upgrade is {price} dollars.", True, BLACK)
    screen.blit(buy, (10, 50))
    screen.blit(stats, (10,30))

    pygame.display.update()
    screen.fill(BLUE)
