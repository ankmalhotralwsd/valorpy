from pygame.locals import *
import pygame
import camera, debug_menu
from object import Object
import mesh
from util import fill_with_zeros

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

objects = []

for x in range(1):
    for z in range(1):
        objects.append(Object(x*100, 0, x*100 + 150.1, 1, 1, 1, mesh.CHICKEN_MESH))



pygame.init()


flags = FULLSCREEN | DOUBLEBUF
resolution = (1024, 576)
screen = pygame.display.set_mode(resolution)


FPS = 60
clock = debug_menu.Clock(60)

mx = resolution[0]/2
my = resolution[1]/2

sens = 0.4

running = True

pygame.mouse.set_pos((resolution[0]/2, resolution[1]/2))

while running:
    clock.tick()
    last_mx = mx
    last_my = my
    mx, my = pygame.mouse.get_pos()
    
    delta_mx = mx - last_mx
    delta_my = my - last_my

    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False
        if(event.type == pygame.KEYDOWN or event.type == pygame.KEYUP):
            cam.handle_input(event.type, event.key)
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
    
    screen.fill(BLACK)

    #draw center of screen
    pygame.draw.circle(screen, (200, 200, 200), (int(resolution[0]/2), int(resolution[1]/2)), 1)


    
    camera.Camera.world_angle[0] += -delta_my * sens
    camera.Camera.world_angle[1] += delta_mx * sens
    camera.Camera.do_rotate()
    cam.do_movement()

    # cube.draw(screen)

    for i in range(len(objects)):
        objects[i].draw(screen)

    #update screen
    clock.render(screen)
    pygame.display.update()

    

pygame.quit()

