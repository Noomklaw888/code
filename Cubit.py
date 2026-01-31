import pygame
import sys

# ------------------ SETUP ------------------
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brick Breaker")

clock = pygame.time.Clock()

# ------------------ PADDLE ------------------
paddle = pygame.Rect(350, 550, 100, 15)
paddle_speed = 7

# ------------------ BALL ------------------
ball = pygame.Rect(390, 300, 15, 15)
ball_dx = 4
ball_dy = -4

# ------------------ BRICKS ------------------
bricks = []
for row in range(5):
    for col in range(10):
        brick = pygame.Rect(col * 78 + 10, row * 30 + 40, 70, 20)
        bricks.append(brick)

# ------------------ GAME LOOP ------------------
while True:
    # EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # INPUT
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.x += paddle_speed

    # BALL MOVEMENT
    ball.x += ball_dx
    ball.y += ball_dy

    # WALL COLLISION
    if ball.left <= 0 or ball.right >= WIDTH-20:
        ball_dx *= -1
    if ball.top <= 0:
        ball_dy *= -1

    # PADDLE COLLISION (SMART BOUNCE)
    if ball.colliderect(paddle):
        ball_dy *= -1

        hit_pos = ball.centerx - paddle.centerx
        ball_dx = hit_pos / 10

    # BRICK COLLISION
    for brick in bricks[:]:
        if ball.colliderect(brick):
            bricks.remove(brick)
            ball_dy *= -1
        pygame.draw.rect(screen, (200, 0, 0), brick)

    # RESPAWN
    if ball.bottom >= HEIGHT:
        ball_dy *= -1
        ball.x=400
        ball.y = 300
        #sys.exit()

    # WIN
    if len(bricks) == 0:
        print("You Win!")
        pygame.quit()
        sys.exit()

    # DRAW
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), paddle)
    pygame.draw.ellipse(screen, (255, 255, 255), ball)

    for brick in bricks:
        pygame.draw.rect(screen, (200, 0, 0), brick)

    pygame.display.flip()
    clock.tick(60)
