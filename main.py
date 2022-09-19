import pygame
import entity
import cube
import math
import camera

pygame.init()

resolution = (1024, 576)
screen = pygame.display.set_mode(resolution)

FPS = 60
clock = pygame.time.Clock()


BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

entities = []

cam = camera.Camera()
cube = cube.Cube(0, 0, 2000, 50, 50, 50)

angle = math.radians(0)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False
        if(event.type == pygame.KEYDOWN or event.type == pygame.KEYUP):
            pass

    
    screen.fill(CYAN)

    #draw center of screen
    pygame.draw.circle(screen, (0, 0, 0), (int(resolution[0]/2), int(resolution[1]/2)), 3)

    # angle += 0.30
    # cube.world_angle = [math.radians(angle), math.radians(angle), 0]

    cube.world_pos = [cube.world_pos[0], cube.world_pos[1]-0.01, 100, 1]
    cube.draw(screen)

    #update screen
    pygame.display.update()


pygame.quit()

