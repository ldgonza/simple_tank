import sys, pygame
pygame.init()

# Setup for handling direction
#
#

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

rotations = dict()
rotations[UP] = pygame.image.load("tank.gif")
rotations[LEFT] = pygame.transform.rotate(rotations[UP], 90)
rotations[DOWN] = pygame.transform.rotate(rotations[UP], 180)
rotations[RIGHT] = pygame.transform.rotate(rotations[UP], 270)

#
# Actual game
#

size = width, height = 800, 600

screen_rect = pygame.Rect(0, 0, 800, 600)
speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

rotation = rotations[UP]
ballrect = rotation.get_rect().move(400, 300);

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    speed = [0, 0]
    keys=pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        speed[1] = -1
        rotation = rotations[UP]
        
    if keys[pygame.K_DOWN]:
        speed[1] = 1
        rotation = rotations[DOWN]

    if keys[pygame.K_LEFT]:
        speed[0] = -1
        rotation = rotations[LEFT]
        
    if keys[pygame.K_RIGHT]:
        speed[0] = 1
        rotation = rotations[RIGHT]

    ballrect = ballrect.move(speed)
    ballrect = ballrect.clamp(screen_rect)
    
    screen.fill(black)
    screen.blit(rotation, ballrect)
    pygame.display.flip()
