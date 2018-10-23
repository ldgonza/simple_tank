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

bullet_rotations = dict()
bullet_rotations[UP] = pygame.image.load("tank.gif")
bullet_rotations[LEFT] = pygame.transform.rotate(bullet_rotations[UP], 90)
bullet_rotations[DOWN] = pygame.transform.rotate(bullet_rotations[UP], 180)
bullet_rotations[RIGHT] = pygame.transform.rotate(bullet_rotations[UP], 270)


#
# Actual game
#

projectile_image = pygame.Surface((10,10))
pygame.draw.circle(projectile_image, (255,255,255), (5,5), 2)

projectile_rect = projectile_image.get_rect()
projectile_speed = [0, 0]
projectile_direction = None

def unshoot():
    """Removes projectile from the game."""

    global projectile_direction, projectile_speed
    
    projectile_direction = None
    projectile_speed = [0, 0]


def shoot(direction):
    """Shoot a single projectile at a time in a given direction.
    
    Direction is UP(0), LEFT(1), DOWN(2), RIGHT(3).

    If a projectile is already in motion, do nothing.
    """

    global projectile_rect, projectile_direction, ballrect, speeds, projectile_speed
    
    if projectile_direction is None:
        projectile_rect.center = ballrect.center
        projectile_direction = direction
        projectile_speed = speeds[direction]

size = width, height = 800, 600

screen_rect = pygame.Rect(0, 0, 800, 600)
speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

rotation = rotations[UP]
ballrect = rotation.get_rect().move(400, 300);

direction = UP

speeds = dict()
speeds[UP] = [0, -1]
speeds[DOWN] = [0, 1]
speeds[LEFT] = [-1, 0]
speeds[RIGHT] = [1, 0]

while 1:
    moving = False
    
    keys=pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        moving = True
        direction = UP
        
    if keys[pygame.K_DOWN]:
        moving = True
        direction = DOWN

    if keys[pygame.K_LEFT]:
        moving = True
        direction = LEFT
        
    if keys[pygame.K_RIGHT]:
        moving = True
        direction = RIGHT
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shoot(direction)

    if moving:
        speed = speeds[direction]
    else:
        speed = [0, 0]

    rotation = rotations[direction]
    ballrect = ballrect.move(speed)
    ballrect = ballrect.clamp(screen_rect)

    if projectile_direction is not None:
        projectile_rect = projectile_rect.move(projectile_speed)

    if not projectile_rect.colliderect(screen_rect):
        unshoot()
    
    screen.fill(black)
    screen.blit(rotation, ballrect)

    if projectile_direction is not None:
        screen.blit(projectile_image, projectile_rect)

    pygame.display.flip()
