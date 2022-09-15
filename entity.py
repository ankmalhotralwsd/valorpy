import pygame


class Entity:
    def __init__(self, color, size, move_speed):
        self.health = 10
        self.damage = 10
        self.color = color
        self.pos = [320, 240]
        self.size = size
        self.move_speed = move_speed


        #input stuff
        self.isWPressed = False
        self.isAPressed = False
        self.isSPressed = False
        self.isDPressed = False

    def move(self, x, y):
        self.pos[0] += x*self.move_speed
        self.pos[1] += y*self.move_speed

    def do_movement(self):
        if self.isWPressed:
            self.move(0, -1)
        if self.isSPressed:
            self.move(0, 1)
        if self.isAPressed:
            self.move(-1, 0)
        if self.isDPressed:
            self.move(1, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.pos[0], self.pos[1]), self.size)

    def handle_input(self, type, key):
        if type == pygame.KEYDOWN:
            if key == pygame.K_w:
                self.isWPressed = True
            if key == pygame.K_s:
                self.isSPressed = True
            if key == pygame.K_a:
                self.isAPressed = True
            if key == pygame.K_d:
                self.isDPressed = True
        
        if type == pygame.KEYUP:
            if key == pygame.K_w:
                self.isWPressed = False
            if key == pygame.K_s:
                self.isSPressed = False
            if key == pygame.K_a:
                self.isAPressed = False
            if key == pygame.K_d:
                self.isDPressed = False




