import pygame


class Entity:
    def __init__(self, color, size, move_speed):
        self.health = 10
        self.damage = 10
        self.color = color
        self.pos = [0, 0]
        self.size = size
        self.move_speed = move_speed


        #input stuff
        isWPressed = False
        isAPressed = False
        isSPressed = False
        isDPressed = False

    def move(self, x, y):
        self.pos[0] += x
        self.pos[1] += y

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.pos[0], self.pos[1]), self.size)

    def handle_input(self, event, key):
        if event.type == pygame.KEYDOWN:
            if key == pygame.K_w:
                self.move()

