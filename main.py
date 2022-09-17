import pygame
import entity
import cube

pygame.init()
screen = pygame.display.set_mode((1024, 576))

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

cube = cube.Cube(250, 200, 0, 50, 50, 50)

angle = 0

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False
        if(event.type == pygame.KEYDOWN or event.type == pygame.KEYUP):
            pass

    
    screen.fill(CYAN)
    angle += .05
    cube.world_angle = [angle, angle, angle]
    cube.draw(screen)
    


    #update screen
    pygame.display.update()




pygame.quit()

