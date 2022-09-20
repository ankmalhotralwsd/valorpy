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

# instantiate entities
cam = camera.Camera()
cube = cube.Cube(0, 0, 150, 50, 50, 50)

angle = math.radians(0)

pygame.mouse.set_visible(False)
pygame.event.set_grab(True)

running = True
while running:
    clock.tick(FPS)
    pygame.event.set_grab(True)
    mx, my = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False
        if(event.type == pygame.KEYDOWN or event.type == pygame.KEYUP):
            cam.handle_input(event.type, event.key)
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
    
    screen.fill(CYAN)

    #draw center of screen
    pygame.draw.circle(screen, (0, 0, 0), (int(resolution[0]/2), int(resolution[1]/2)), 3)

    angle += 0.20
    cube.world_angle = [math.radians(angle), math.radians(angle), math.radians(angle)]
    cam.do_movement()
    
    cube.draw(screen)

    #update screen
    pygame.display.update()


pygame.quit()

