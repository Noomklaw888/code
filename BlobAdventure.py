'''Blob Adventure!
Arrow keys or WASD to move
Space to shoot
Shoot the evil Slimies or they will get you!
-Noomklaw
'''
import pygame
import random

pygame.init()
font = pygame.font.SysFont("Arial", 32)



BLOB  = (0, 255, 125)
GRASS = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255,0,0)
WHITE = (255,255,255)
print("Running...")

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blob adventure v1")
clock = pygame.time.Clock()

px = 100
py = 100
speed = 5
bxc = 2* speed
byc = 0
bullet_timer = 0
lives = 5

bullets = [
    ]
enemies = []
timer = 0
ex = 0
ey = 350
running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        bxc = 2 * speed
        byc = 0
        px += speed
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        px -= speed
        bxc = -2 * speed
        byc = 0
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        byc = 2 * speed
        bxc = 0
        py += speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        byc = -2 * speed
        bxc = 0
        py -= speed
    if keys[pygame.K_SPACE] and bullet_timer < 0:
        bullet_timer = 25
        x = px
        y = py
        bullets.append({
            "rect": pygame.Rect(x, y, 10, 10),
            "dx": bxc,
            "dy": byc
            })

    for bullet in bullets[:]:
        bullet["rect"].x += bullet["dx"]
        bullet["rect"].y += bullet["dy"]
        if bullet["rect"].x > WIDTH or bullet["rect"].x < 0:
            bullets.remove(bullet)
        if bullet["rect"].y > WIDTH or bullet["rect"].y < 0:
            bullets.remove(bullet)
    timer += 1
    if timer % 100== 0:
        ey = random.randint(0,700-30)
        enemies.append(pygame.Rect(ex,ey,30, 30))
        
        blobrect = pygame.Rect(px, py, 50,50)
        
    for enemy in enemies:
        erect = pygame.Rect(enemy.x, enemy.y, 30, 30)
        if px > enemy.x:
            enemy.x += 1
        if px < enemy.x:
            enemy.x -= 1            
        if py > enemy.y:
            enemy.y += 1
        if py < enemy.y:
            enemy.y -= 1
        for bullet in bullets[:]:
            if erect.colliderect(bullet["rect"]):
                enemies.remove(enemy)
        if erect.colliderect(blobrect):
            enemies.remove(enemy)
            lives -= 1

        
        
        
    bullet_timer -= 1        
    px = max(0, min(px, WIDTH - 30))
    py = max(0, min(py, HEIGHT - 30))

    screen.fill(GRASS)

    pygame.draw.rect(screen, BLOB,  (px, py, 30, 30))
    pygame.draw.rect(screen, BLACK, (px+5, py + 5, 5, 20))
    pygame.draw.rect(screen, BLACK, (px + 20, py + 5, 5, 20))
    for bullet in bullets:
        pygame.draw.rect(screen, RED, bullet["rect"])

    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)
        pygame.draw.rect(screen, WHITE, (enemy.x+5, enemy.y+5, 20, 20))
        pygame.draw.rect(screen, BLACK, (enemy.x+random.randint(5,15), enemy.y+random.randint(5,15), 10, 10))

    text_surface = font.render(f"Lives left: {str(lives)}", True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.center = (WIDTH // 2), 16
    screen.blit(text_surface, text_rect)

    if lives == 0:
        running = False


    pygame.display.update()
    clock.tick(60)
pygame.quit
print("Game over!")
