import math
import util
import pygame

resolution = (1024, 576)
aspect_ratio = resolution[1]/resolution[0]
field_of_view = 103
field_of_view_scaling_factor = math.degrees(math.tan(math.radians(field_of_view/2)))

yScale = 1.0 / math.tan(math.radians(field_of_view/2))
xScale = yScale / aspect_ratio
nearmfar = 1 - 100

far = 100
near = 1

class Camera:
    def __init__(self):
        Camera.world_pos = [0, 0, -1, 1]
        Camera.inverse_pos = [0, 0, -1, 1]

        self.move_speed = 10
        self.isWPressed = False
        self.isAPressed = False
        self.isSPressed = False
        self.isDPressed = False

    def move(self, x, y, z):
        Camera.world_pos[0] += x*self.move_speed
        Camera.world_pos[1] += y*self.move_speed
        Camera.world_pos[2] += z*self.move_speed

    @staticmethod
    def convert_to_camera_space(a):
        Camera.inverse_pos[0] = -Camera.world_pos[0]
        Camera.inverse_pos[1] = -Camera.world_pos[1]
        Camera.inverse_pos[2] = -Camera.world_pos[2]
        
        c = list(a)

        c[0] = a[0] + Camera.inverse_pos[0]
        c[1] = a[1] + Camera.inverse_pos[1]
        c[2] = a[2] + Camera.inverse_pos[2]
        return c

    def do_movement(self):
        if self.isWPressed:
            self.move(0, 0, 1)
        if self.isSPressed:
            self.move(0, 0, -1)
        if self.isAPressed:
            self.move(-1, 0, 0)
        if self.isDPressed:
            self.move(1, 0, 0)

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

def perspective_x_coords(a):
    PERSPECTIVE_MATRIX = [[xScale, 0, 0, 0],
                            [0, yScale, 0, 0],
                            [0, 0, (far + near) / nearmfar, -1],
                            [0, 0, 2*far*near / nearmfar, 0]]
    return util.matrix_x_vector(PERSPECTIVE_MATRIX, a)