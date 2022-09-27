import math
from rotation_matrices import rotate_y, rotate_x, rotate_z
import util
import pygame

resolution = (1024, 576)

aspect_ratio = resolution[1]/resolution[0]
field_of_view = 100

yScale = 1.0 / math.tan(math.radians(field_of_view/2))
xScale = yScale / aspect_ratio


far = 100
near = 1

nearmfar = near - far


class Camera:
    def __init__(self):
        Camera.world_pos = [0, 0, -1, 1]
        Camera.inverse_pos = [0, 0, -1, 1]

        Camera.world_angle = [math.radians(0), math.radians(0), math.radians(0)]

        Camera.transform_matrix = [[1, 0, 0, 0],
                                    [0, 1, 0, 0],
                                    [0, 0, 1, 0],
                                    [0, 0, 0, 1]]
        Camera.unrotated_forward = [0, 0, 1, 0]
        Camera.forward = [0, 0, 1, 0]

        self.move_speed = 0.5
        self.isWPressed = False
        self.isAPressed = False
        self.isSPressed = False
        self.isDPressed = False

        self.isUpPressed = False
        self.isDownPressed = False



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
    
    @staticmethod
    def do_rotate():
        Camera.forward = list(Camera.unrotated_forward)
        Camera.forward = rotate_x(Camera.forward, Camera.world_angle[0])
        Camera.forward = rotate_y(Camera.forward, Camera.world_angle[1])
        Camera.forward = rotate_z(Camera.forward, Camera.world_angle[2])
        #print(Camera.forward)
    
    def move(self, x, y, z):

        

        Camera.world_pos[0] += x*self.move_speed
        Camera.world_pos[1] += y*self.move_speed
        Camera.world_pos[2] += z*self.move_speed

    def do_movement(self):
        if self.isWPressed:
            self.move(0, 0, 1)
        if self.isSPressed:
            self.move(0, 0, -1)
        if self.isAPressed:
            self.move(1, 0, 0)
        if self.isDPressed:
            self.move(-1, 0, 0)
        if self.isUpPressed:
            self.move(0, 1, 0)
        if self.isDownPressed:
            self.move(0, -1, 0)

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
            if key == pygame.K_UP:
                self.isUpPressed = True
            if key == pygame.K_DOWN:
                self.isDownPressed = True
        
        if type == pygame.KEYUP:
            if key == pygame.K_w:
                self.isWPressed = False
            if key == pygame.K_s:
                self.isSPressed = False
            if key == pygame.K_a:
                self.isAPressed = False
            if key == pygame.K_d:
                self.isDPressed = False
            if key == pygame.K_UP:
                self.isUpPressed = False
            if key == pygame.K_DOWN:
                self.isDownPressed = False

def perspective_x_coords(a):
    PERSPECTIVE_MATRIX = [[xScale, 0, 0, 0],
                            [0, yScale, 0, 0],
                            [0, 0, (far + near) / nearmfar, -1],
                            [0, 0, 2*far*near / nearmfar, 0]]
    return util.matrix_x_vector(PERSPECTIVE_MATRIX, a)

def world_x_coords(a):
    VIEW_MATRIX = [[1, 0, 0, 0],
                            [0, 1, 0, 0],
                            [0, 0, 1, 0],
                            [0, 0, 0, 1]]
    return util.matrix_x_vector(VIEW_MATRIX, a)