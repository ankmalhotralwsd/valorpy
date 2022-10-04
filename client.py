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

mx = resolution[0]/2
my = resolution[1]/2

sens = 0.4

running = True

pygame.mouse.set_pos((resolution[0]/2, resolution[1]/2))

while running:
    clock.tick(FPS)
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
    pygame.draw.circle(screen, (0, 0, 0), (int(resolution[0]/2), int(resolution[1]/2)), 3)


    
    camera.Camera.world_angle[0] += -delta_my * sens
    camera.Camera.world_angle[1] += delta_mx * sens
    camera.Camera.do_rotate()

    #cube.world_angle[0] = math.radians(mouseY)
    #cube.world_angle[1] = math.radians(mouseX)
    cam.do_movement()

    # camera.Camera.move_obj_camera_forward(cube, 5)

    cube.draw(screen)

    # endpoint = util.vector_plus_vector([0, 0, 50, 1], util.vector_x_scalar(camera.Camera.forward, 5, [3]), [3])
    # line.model_space_vertices = [[0, 0, 50, 1], endpoint]
    # line.draw(screen)

    #update screen
    pygame.display.update()

    

pygame.quit()

