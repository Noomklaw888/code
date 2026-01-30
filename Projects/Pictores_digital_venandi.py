import pygame
import random
pygame.init()
pygame.display.set_caption("Pictores digital venandi")

'''
translate from latin to english
RED = Predator
OTHERS = Painters
Press Q to move Cube artists to Cubite
Press Space to move Cube artists to center
If all you can see is Cubite in the center, press Q
seagreen: Cubit
yellow: Cubet
blue: Cubot
white: Cubat
red: Cubite
'''
#colors
GREEN = (0,255,0)
DARKGREEN = (0,200,0)
RED = (255,0,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
YELLOW=(255,255,0)
SEAGREEN=(0,225,182)
WIDTH = 800#Pocket:200
HEIGHT = 600#Pocket:200
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#stuff
ex = 775
ey = 555
rx = 0
ry = 0
rx1 = 0
ry1 = 0
rx2 = 0
ry2 = 0
rx3 = 0
ry3 = 0

food = [
    ]

for i in range(100):
   numnum = pygame.Rect(random.randint(0, WIDTH-10), random.randint(0, HEIGHT-10), 10, 10)
   food.append(numnum)

#Run
clock = pygame.time.Clock()
running = True
timer = 0

while running:
   clock.tick(60)
   timer += 1
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False
   #rects        
   e = pygame.Rect(ex, ey, 25, 25)
   p1 = pygame.Rect(rx1, ry1, 25, 25)
   p2 = pygame.Rect(rx2, ry2, 25, 25)
   p3 = pygame.Rect(rx3, ry3, 25, 25)
   p = pygame.Rect(rx, ry, 25, 25)

   #move
   #p
   if abs(rx-ex) < 50 or abs(ry-ey)<50:
       
       if rx-ex<0:
           rx-= 5
           ex -= random.randint(3, 7)
       elif rx-ex>0:
           rx+= 10
           ex += random.randint(3, 7)
       if ry-ey<0:
           ry-= 5
           ey -= random.randint(3, 7)
       elif ry-ey>0:
           ry+= 10
           ey += random.randint(3, 7)
   else:
       rx -= random.randint(-1,1)*5
       ry -= random.randint(-1,1)*5
       #p1
   if abs(rx1-ex) < 50 or abs(ry1-ey)<50:
       
       if rx1-ex<0:
           rx1-= 5
           ex -= random.randint(3, 7)
       elif rx1-ex>0:
           rx1+= 10
           ex += random.randint(3, 7)
       if ry1-ey<0:
           ry1-= 5
           ey -= random.randint(3, 7)
       elif ry1-ey>0:
           ry1+= 10
           ey += random.randint(3, 7)
   else:
       rx1 += random.randint(-1,1)*5
       ry1 += random.randint(-1,1)*5
       #p2
   if abs(rx2-ex) < 50 or abs(ry2-ey)<50:
       
       if rx2-ex<0:
           rx2-= 5
           ex -= random.randint(3, 7)
       elif rx2-ex>0:
           rx2+= 10
           ex += random.randint(3, 7)
       if ry2-ey<0:
           ry2-= 5
           ey -= random.randint(3, 7)
       elif ry2-ey>0:
           ry2+= 10
           ey += random.randint(3, 7)
   else:
       rx2 -= random.randint(-1,1)*5
       ry2 -= random.randint(-1,1)*5
       #p3
   if abs(rx3-ex) < 50 or abs(ry3-ey)<50:
       
       if rx3-ex<0:
           rx3-= 5
           ex -= random.randint(3, 7)
       elif rx3-ex>0:
           rx3+= 10
           ex += random.randint(3, 7)
       if ry3-ey<0:
           ry3-= 5
           ey -= random.randint(3, 7)
       elif ry3-ey>0:
           ry3+= 10
           ey += random.randint(3, 7)
   else:
       rx3 += random.randint(-1,1)*5
       ry3 += random.randint(-1,1)*5
   
    #bounds
   if rx > WIDTH-25:
       rx=WIDTH-25
   if rx < 0:
       rx=0
   if ry > HEIGHT-25:
       ry = HEIGHT-25
   if ry < 0:
       ry = 0
       
   if rx1 > WIDTH-25:
       rx1=WIDTH-25
   if rx1 < 0:
       rx1=0
   if ry1 > HEIGHT-25:
       ry1 = HEIGHT-25
   if ry1 < 0:
       ry1 = 0
       
   if rx2 > WIDTH-25:
       rx2=WIDTH-25
   if rx2 < 0:
       rx2=0
   if ry2 > HEIGHT-25:
       ry2 = HEIGHT-25
   if ry2 < 0:
       ry2 = 0
       
   if rx3 > WIDTH-25:
       rx3=WIDTH-25
   if rx3 < 0:
       rx3=0
   if ry3 > HEIGHT-25:
       ry3 = HEIGHT-25
   if ry3 < 0:
       ry3 = 0

   if ex > WIDTH-25:
       ex=WIDTH-25
   if ex < 0:
       ex=0
   if ey > WIDTH-25:
       ey = WIDTH-25
   if ey < 0:
       ey = 0
    #respawn
   if e.colliderect(p):
       ry = HEIGHT/2
       rx = WIDTH/2
   if e.colliderect(p1):
       ry1 = HEIGHT/2
       rx1= WIDTH/2
   if e.colliderect(p2):
       ry2 = HEIGHT/2
       rx2 = WIDTH/2
   if e.colliderect(p3):
       ry3 = HEIGHT/2
       rx3= WIDTH/2
   keys = pygame.key.get_pressed()
   if keys[pygame.K_SPACE]:
       rx=WIDTH/2
       ry=HEIGHT/2
       rx1=WIDTH/2
       ry1=HEIGHT/2
       rx2=WIDTH/2
       ry2=HEIGHT/2
       rx3=WIDTH/2
       ry3=HEIGHT/2
   if keys[pygame.K_q]:
       rx=ex+25
       ry=ey+25
       rx1=ex-25
       ry1=ey+25
       rx2=ex+25
       ry2=ey-25
       rx3=ex-25
       ry3=ey-25

    #draw
#   screen.fill(GREEN)
   pygame.draw.rect(screen, SEAGREEN, p)
   pygame.draw.rect(screen, BLUE, p1)
   pygame.draw.rect(screen, WHITE, p2)
   pygame.draw.rect(screen, YELLOW, p3)
   pygame.draw.rect(screen, BLACK, (rx, ry, 10, 20))
   pygame.draw.rect(screen, BLACK, (rx+15, ry, 10, 20))
   pygame.draw.rect(screen, BLACK, (rx1, ry1, 10, 20))
   pygame.draw.rect(screen, BLACK, (rx1+15, ry1, 10, 20))
   pygame.draw.rect(screen, BLACK, (rx2, ry2, 10, 20))
   pygame.draw.rect(screen, BLACK, (rx2+15, ry2, 10, 20))
   pygame.draw.rect(screen, BLACK, (rx3, ry3, 10, 20))
   pygame.draw.rect(screen, BLACK, (rx3+15, ry3, 10, 20))
   pygame.draw.rect(screen, RED, e)
   pygame.draw.rect(screen, BLACK, (ex, ey, 10, 20))
   pygame.draw.rect(screen, BLACK, (ex+15, ey, 10, 20))
   for numnum in food[:]:
       pygame.draw.rect(screen, DARKGREEN, numnum)
   pygame.display.flip()

pygame.quit()  

    
