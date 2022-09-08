import pygame
import entity


pygame.init()
screen = pygame.display.set_mode((640, 480))

BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)


player = entity.Entity(RED, 15)

running = True
while running:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False
        if(event.type == pygame.KEYDOWN):
            if event.key == pygame.K_w:
                player.move(0, -5)
            if event.key == pygame.K_d:
                player.move(5, 0)
            if event.key == pygame.K_s:
                player.move(0, 5)
            if event.key == pygame.K_a:
                player.move(-5, 0)
    screen.fill(CYAN)
    player.draw(screen)
    
    pygame.display.update()




pygame.quit()

