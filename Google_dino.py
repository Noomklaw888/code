import pygame
import random
pygame.init()

#colors
GREY = (148, 148, 148)
GREEN = (70, 163, 26)
BROWN = (200, 100, 50)
BLACK = (0,0,0)
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Google Dinosaur")

#dino
player_y=400
dino = pygame.Rect(200, player_y, 25, 50)
y_velocity = 0
jump_strength = -15
gravity = 0.8

#ground
ground = pygame.Rect(-50000000, 560, 100000000, 40)

#cactus
cheight = 0
cx = 0
cwidth = 0
cactus = pygame.Rect(cx, 560-cheight, cwidth, cheight)


#run
clock = pygame.time.Clock()
running = True
score = 0
timer = 0
font = pygame.font.Font(None, 36)

while running:
    clock.tick(60)
    timer += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    dino_rect = pygame.Rect(200, player_y, 25, 50)

#jump
    if keys[pygame.K_UP] and on_ground == True or keys[pygame.K_SPACE] and on_ground == True:
        y_velocity = jump_strength
    y_velocity += gravity
    player_y += y_velocity

    #ground
    if dino_rect.colliderect(ground) and y_velocity >= 0:
        player_y = ground.top - 50
        y_velocity = 0
        on_ground = True
    else:
        on_ground = False
    
    #cactus
    cactus = pygame.Rect(cx, 560-cheight, cwidth, cheight)
    if timer % 100 == 0:
        cheight = random.randint(1,3) * 25
        cx = 800
        cwidth = random.randint(1,2) * 25
    cx -= 10


    if dino_rect.colliderect(cactus):
        running = False
        gameovertext = font.render(f"score: {score}", True, BLACK)
        screen.blit(gameovertext, (400, 300))
        
        print(f"Your score was {score}!")

    #draw
    font = pygame.font.Font(None, 36)

    scoretext = font.render(f"score: {score}", True, BLACK)
    if timer % 7 == 0:
        score += 1
    #draw
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, GREY, (200, player_y, 25, 50))
    pygame.draw.rect(screen, GREY, (180, player_y + 30, 20, 10))
    pygame.draw.rect(screen, GREY, (200, player_y, 45, 30))
    pygame.draw.rect(screen, BROWN, ground)
    screen.blit(scoretext, (10, 10))
    pygame.draw.rect(screen, GREEN, cactus)
    pygame.display.flip()

pygame.quit()
