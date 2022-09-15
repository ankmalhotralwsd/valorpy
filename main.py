import pygame
import entity


pygame.init()
screen = pygame.display.set_mode((640, 480))

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
player = entity.Entity(RED, 15, 1)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False
        if(event.type == pygame.KEYDOWN or event.type == pygame.KEYUP):
            pass
            player.handle_input(event.type, event.key)
    player.do_movement()
    
    screen.fill(CYAN)

    #draw objects
    player.draw(screen)
    
    #update screen
    pygame.display.update()




pygame.quit()

