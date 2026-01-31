import pygame

pygame.init()

# ---------------- COLORS ----------------
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SEAGREEN = (0, 255, 182)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

# ---------------- SCREEN ----------------
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cubit Platformer")

clock = pygame.time.Clock()
running = True

# ---------------- PLAYER SETTINGS ----------------
player_width, player_height = 50, 50
player_speed = 5

# Player 1
player_x = 100
player_y = HEIGHT - player_height - 100
y_velocity = 0
on_ground = False

# Player 2
player_x2 = 150
player_y2 = HEIGHT - player_height - 100
y_velocity2 = 0
on_ground2 = False

# ---------------- PHYSICS ----------------
gravity = 0.8
jump_strength = -15

# ---------------- COYOTE TIME ----------------
coyote_time = 0.1  # seconds
coyote_timer = 0
coyote_timer2 = 0

# ---------------- HOVER ----------------
hover_speed = 0        # downward speed limit
max_hover_ascend = 0  # upward speed limit
max_hover_time = 1.5   # seconds
hover_timer = max_hover_time

# ---------------- CAMERA ----------------
camera_x = 0

# ---------------- PLATFORMS ----------------
platforms = [
    pygame.Rect(-50000000, HEIGHT - 40, 100000000, 40),  # ground
    pygame.Rect(200, 450, 150, 20),
    pygame.Rect(450, 350, 150, 20),
    pygame.Rect(800, 300, 150, 20),
    pygame.Rect(1100, 250, 150, 20),
    pygame.Rect(1500, 450, 20, 20),
    pygame.Rect(1600, 300, 20, 20),
    pygame.Rect(1800, 200, 20, 20),
    pygame.Rect(2000, 100, 150, 20),
]

# ---------------- SPIKES ----------------
spikes = [
    pygame.Rect(1150, 230, 50, 20),
    pygame.Rect(800, 320, 150, 400),
    pygame.Rect(1400, 0, 20, 500),
    pygame.Rect(2200, 140, 200, 400),
]

# ---------------- CHECKPOINTS ----------------
checkpoints = [
    pygame.Rect(400, 420, 40, 40),
    pygame.Rect(900, 270, 40, 40),
    pygame.Rect(2050, 70, 40, 40),
]

checkpoint_x = 100
checkpoint_y = HEIGHT - player_height - 100

# ---------------- BUTTONS & BRIDGES ----------------
buttons = [
    pygame.Rect(600, 520, 40, 20),
    pygame.Rect(1300, 230, 40, 20),
    pygame.Rect(2050, 70, 40, 40),
]

# Define how many players are required per button
button_required_players = [1, 1, 1]

bridges = [
    pygame.Rect(750, 400, 200, 20),
    pygame.Rect(1400, 200, 200, 20),
    pygame.Rect(2199, 120, 220, 400)
]

bridge_active = [False] * len(bridges)

# ---------------- GAME LOOP ----------------
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # -------- MOVEMENT --------
    if keys[pygame.K_LEFT] and not keys[pygame.K_SPACE]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]:
        player_x += player_speed
    if keys[pygame.K_UP] and coyote_timer > 0:
        y_velocity = jump_strength
        coyote_timer = 0

    if keys[pygame.K_a]:
        player_x2 -= player_speed
    if keys[pygame.K_d]:
        player_x2 += player_speed
    if keys[pygame.K_w] and coyote_timer2 > 0:
        y_velocity2 = jump_strength
        coyote_timer2 = 0

    # -------- GRAVITY & HOVER --------

#'''
    if not keys[pygame.K_SPACE]:
        y_velocity += gravity
        player_y += y_velocity
        if on_ground:
            hover_timer = max_hover_time
#'''

    y_velocity2 += gravity

    player_y2 += y_velocity2

    # -------- RECTANGLES --------
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    player_rect2 = pygame.Rect(player_x2, player_y2, player_width, player_height)

    # -------- COLLISIONS --------
    on_ground = False
    on_ground2 = False

    for platform in platforms:
        if player_rect.colliderect(platform) and y_velocity >= 0:
            player_y = platform.top - player_height
            y_velocity = 0
            on_ground = True

        if player_rect2.colliderect(platform) and y_velocity2 >= 0:
            player_y2 = platform.top - player_height
            y_velocity2 = 0
            on_ground2 = True

    # Player-on-player standing
    if player_rect2.colliderect(player_rect) and y_velocity2 >= 0:
        player_y2 = player_rect.top - player_height
        y_velocity2 = 0
        on_ground2 = True

    # -------- BRIDGE COLLISIONS --------
    for i, bridge in enumerate(bridges):
        if bridge_active[i]:
            if player_rect.colliderect(bridge) and y_velocity >= 0:
                player_y = bridge.top - player_height
                y_velocity = 0
                on_ground = True
            if player_rect2.colliderect(bridge) and y_velocity2 >= 0:
                player_y2 = bridge.top - player_height
                y_velocity2 = 0
                on_ground2 = True

    # -------- COYOTE TIMER UPDATE --------
    coyote_timer = coyote_time if on_ground else max(coyote_timer - 1/60, 0)
    coyote_timer2 = coyote_time if on_ground2 else max(coyote_timer2 - 1/60, 0)

    # -------- CHECKPOINT ACTIVATION --------
    for cp in checkpoints:
        if player_rect.colliderect(cp) or player_rect2.colliderect(cp):
            checkpoint_x = cp.x
            checkpoint_y = cp.y - player_height

    # -------- SPIKE DEATH --------
    for spike in spikes:
        if player_rect.colliderect(spike):
            player_x = checkpoint_x
            player_y = checkpoint_y
            y_velocity = 0

        if player_rect2.colliderect(spike):
            player_x2 = checkpoint_x + 60
            player_y2 = checkpoint_y
            y_velocity2 = 0

    # -------- BUTTON CHECK --------
    for i, button in enumerate(buttons):
        count = 0
        if player_rect.colliderect(button):
            count += 1
        if player_rect2.colliderect(button):
            count += 1
        bridge_active[i] = count >= 1

    # -------- CAMERA --------
    camera_x = player_x - WIDTH // 2

    # -------- DRAW --------
    screen.fill(BLUE)

    # Draw platforms
    for platform in platforms:
        pygame.draw.rect(screen, BLACK, (platform.x - camera_x, platform.y, platform.width, platform.height))

    # Draw spikes
    for spike in spikes:
        pygame.draw.rect(screen, RED, (spike.x - camera_x, spike.y, spike.width, spike.height))

    # Draw checkpoints
    for cp in checkpoints:
        pygame.draw.rect(screen, GREEN, (cp.x - camera_x, cp.y, cp.width, cp.height))

    # Draw bridges
    for i, bridge in enumerate(bridges):
        if bridge_active[i]:
            pygame.draw.rect(screen, BLACK, (bridge.x - camera_x, bridge.y, bridge.width, bridge.height))

    # Draw buttons
    for i, button in enumerate(buttons):
        color = GREEN if bridge_active[i] else RED
        pygame.draw.rect(screen, color, (button.x - camera_x, button.y, button.width, button.height))

    # Draw players
    draw_x = player_x - camera_x
    pygame.draw.rect(screen, SEAGREEN, (draw_x, player_y, player_width, player_height))
    pygame.draw.rect(screen, BLACK, (draw_x, player_y, 20, 30))
    pygame.draw.rect(screen, BLACK, (draw_x + 30, player_y, 20, 30))

    draw_x2 = player_x2 - camera_x
    pygame.draw.rect(screen, YELLOW, (draw_x2, player_y2, player_width, player_height))
    pygame.draw.rect(screen, BLACK, (draw_x2, player_y2, 20, 30))
    pygame.draw.rect(screen, BLACK, (draw_x2 + 30, player_y2, 20, 30))

    pygame.display.update()

pygame.quit()
