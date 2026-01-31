import pygame
import time
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0,0,255)
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Picture!")

listy = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1]

]

for row in range(10):
    for col in range(10):
        listy[row][col] = -1

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    mouse_presses = pygame.mouse.get_pressed()

    if mouse_presses[0]:
        mx, my = pygame.mouse.get_pos()
        listy[my//50][mx//50] = listy[my//50][mx//50] * -1
        time.sleep(0.1)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        for row in range(10):
            for col in range(10):
                listy[row][col] = -1
        
    screen.fill(BLACK)

    for row in range(10):
        for col in range(10):
            if listy[row][col] == 1:
                pygame.draw.rect(
                    screen,
                    WHITE,
                    ((50 * col), (50 * row), 50, 50)
                )
            else:
                pygame.draw.rect(
                    screen,
                    BLUE,
                    ((50 * col), (50 * row), 50, 50)
                )

    pygame.display.update()
    clock.tick(60)
