import pygame
import random

d=0
# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blocky space")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Player
player_width, player_height = 50, 70
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10
player_speed = 5

# Bullet
bullet_width, bullet_height = 5, 10
bullet_speed = 7
bullets = []
bullet_cooldown = 300  # milliseconds
last_shot_time = 0
maxi = 10

# Enemies
enemies = []
enemy_spawn_delay = 1500  # milliseconds
pygame.time.set_timer(pygame.USEREVENT, enemy_spawn_delay)
enemy_speed = 2

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)  # 60 FPS

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.USEREVENT:
            # Randomly spawn big or small enemy
            var = random.random()
            if var > 0.8:
                # Big enemy
                ex = random.randint(0, WIDTH - 100)
                ey = -100
                enemies.append({"rect": pygame.Rect(ex, ey, 100, 100), "type": "big"})
            elif var < 0.3:
                # Moving enemy
                ex = random.randint(0, WIDTH - 50)
                ey = -50
                enemies.append({"rect": pygame.Rect(ex, ey, 50, 50), "type": "moving"})
            else:
                # Small enemy
                ex = random.randint(0, WIDTH - 50)
                ey = -50
                enemies.append({"rect": pygame.Rect(ex, ey, 50, 50), "type": "small"})

    # Key states
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x - player_speed > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x + player_speed < WIDTH - player_width:
        player_x += player_speed
    if keys[pygame.K_SPACE]:
        current_time = pygame.time.get_ticks()
        if current_time - last_shot_time > bullet_cooldown and len(bullets) < maxi:
            if d==2:
                bullets.append(pygame.Rect(player_x + player_width//2 - bullet_width//2 - 50, player_y, bullet_width, bullet_height))
                bullets.append(pygame.Rect(player_x + player_width//2 - bullet_width//2 + 50, player_y, bullet_width, bullet_height))
            else:
                bullets.append(pygame.Rect(player_x + player_width//2 - bullet_width//2, player_y, bullet_width, bullet_height))
            last_shot_time = current_time

    # Move bullets
    for bullet in bullets[:]:
        bullet.y -= bullet_speed
        if bullet.y < 0:
            bullets.remove(bullet)

    # Move enemies
    for enemy in enemies[:]:
        enemy["rect"].y += enemy_speed
        if enemy["type"] == "moving":
            enemy["rect"].x += random.randint(-10,10)
        if enemy["rect"].y > HEIGHT:
            enemies.remove(enemy)
        # Collision with bullets
        for bullet in bullets[:]:
            if enemy["rect"].colliderect(bullet):
                bullets.remove(bullet)
                if enemy["type"] == "big":
                    ex, ey = enemy["rect"].x, enemy["rect"].y
                    # Split into 2 smaller enemies
                    enemies.append({"rect": pygame.Rect(ex-50, ey, 50, 50), "type": "small"})
                    enemies.append({"rect": pygame.Rect(ex + 50, ey, 50, 50), "type": "small"})
                enemies.remove(enemy)
                score += 1
 
    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, (player_x-10, player_y+50, player_width+20, 20))
    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_width, player_height))
    pygame.draw.rect(screen, WHITE, (player_x+15, player_y-20, 20, player_height))

# Player

    for bullet in bullets:
        pygame.draw.rect(screen, RED, bullet)

    for enemy in enemies:
        if enemy["type"] == "big":
            color = RED
            
        elif enemy["type"] == "moving":
            color = YELLOW
        else:
            color =GREEN
        
        pygame.draw.rect(screen, color, enemy["rect"])

    # Draw score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.update()

    if score == 25:
        d=2
    if score == 50:
        bullet_width=5
        bullet_speed=20
    if score == 75:
        bullet_width =150
        d=0


pygame.quit()
