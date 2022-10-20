import pygame

class Clock:
    def __init__(self, max_fps):
        self.max_fps = max_fps
        self.clock = pygame.time.Clock()

        self.font = pygame.font.SysFont("Consolas", 35)
        self.text = self.font.render(str(round(self.clock.get_fps())), True, (255,255,255))

    def render(self, screen):
        self.text = self.font.render(str(round(self.clock.get_fps())), True, (255,255,255))
        screen.blit(self.text, (800, 50))
    
    def tick(self):
        self.clock.tick(self.max_fps)