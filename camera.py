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
        Camera.world_pos = [0, 0, 0, 1]
        Camera.inverse_pos = [0, 0, 0, 1]

        Camera.world_angle = [math.radians(0), math.radians(0), math.radians(0)]

        Camera.transform_matrix = [[1, 0, 0, 0],
                                    [0, 1, 0, 0],
                                    [0, 0, 1, 0],
                                    [0, 0, 0, 1]]
        Camera.unrotated_forward = [0, 0, 1, 0]
        Camera.forward = [0, 0, 1, 0]

        Camera.move_speed = 0.5
        Camera.isWPressed = False
        Camera.isAPressed = False
        Camera.isSPressed = False
        Camera.isDPressed = False

        Camera.isUpPressed = False
        Camera.isDownPressed = False



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
        Camera.forward = rotate_x(Camera.forward, math.radians(Camera.world_angle[0]))
        Camera.forward = rotate_y(Camera.forward, math.radians(Camera.world_angle[1]))
    
    def move(self, x): 
        Camera.world_pos = util.vector_plus_vector(Camera.world_pos, util.vector_x_scalar(Camera.forward, x, [3]), [3]) 
        print(Camera.forward)
    def do_movement(self):
        Camera.do_rotate()
        if self.isWPressed:
            self.move(self.move_speed)
        if self.isSPressed:
            self.move(-self.move_speed)
        # if self.isAPressed:
        #     self.move(1, 0, 0)
        # if self.isDPressed:
        #     self.move(-1, 0, 0)
        # if self.isUpPressed:
        #     self.move(0, 1, 0)
        # if self.isDownPressed:
        #     self.move(0, -1, 0)

    @staticmethod
    def handle_input(type, key):

        if type == pygame.KEYDOWN:
            if key == pygame.K_w:
                Camera.isWPressed = True
            if key == pygame.K_s:
                Camera.isSPressed = True
            if key == pygame.K_a:
                Camera.isAPressed = True
            if key == pygame.K_d:
                Camera.isDPressed = True
            if key == pygame.K_UP:
                Camera.isUpPressed = True
            if key == pygame.K_DOWN:
                Camera.isDownPressed = True
        
        if type == pygame.KEYUP:
            if key == pygame.K_w:
                Camera.isWPressed = False
            if key == pygame.K_s:
                Camera.isSPressed = False
            if key == pygame.K_a:
                Camera.isAPressed = False
            if key == pygame.K_d:
                Camera.isDPressed = False
            if key == pygame.K_UP:
                Camera.isUpPressed = False
            if key == pygame.K_DOWN:
                Camera.isDownPressed = False

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