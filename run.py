import pygame
import entity
import cube
import math
import camera
import line
import util

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

cube = cube.Cube(0, 0, 300, 50, 50, 50)
line = line.Line(0, 0, 50, 0, 0, 50, (0, 0, 255))

angle = math.radians(0)

# pygame.mouse.set_visible(False)
# pygame.event.set_grab(True)

running = True
while running:
    clock.tick(FPS)
    
    mx, my = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False
        if(event.type == pygame.KEYDOWN or event.type == pygame.KEYUP):
            cam.handle_input(event.type, event.key)
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
    
    screen.fill(GRAY)

    #draw center of screen
    pygame.draw.circle(screen, (0, 0, 0), (int(resolution[0]/2), int(resolution[1]/2)), 3)

    
    
    cam.do_movement()
    
    mouseY = -(my - (575/2)) / (575/2) * 180
    mouseX = (mx - (1024/2)) / (1024/2) * 180
    
    camera.Camera.world_angle[0] = mouseY
    camera.Camera.world_angle[1] = mouseX
    camera.Camera.do_rotate()

    cube.draw(screen)

    endpoint = util.vector_plus_vector([0, 0, 50, 1], util.vector_x_scalar(camera.Camera.forward, 5, [3]), [3])
    line.model_space_vertices = [[0, 0, 50, 1], endpoint]
    line.draw(screen)

    #update screen
    pygame.display.update()

    

pygame.quit()

