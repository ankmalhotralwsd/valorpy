import pygame
from util import weird_vector_to_matrix
from util import convert_vector_to_int
from predefined_matrices import CUBE_VERTEX_MATRIX
import camera_matrices

class Cube:
    def __init__(self, x, y, z, x_s, y_s, z_s):
        self.origin = [x, y, z, 1]
        self.scale = [x_s, y_s, z_s]
        self.angle = 0
        self.vertices = weird_vector_to_matrix(self.scale, CUBE_VERTEX_MATRIX)
    def get_vertices(self):
        return self.vertices
    
    def draw(self, screen):
        for i in range(len(self.vertices)):
            # print(self.vertices[i])
            pass
            #pygame.draw.circle(screen, (255, 255, 255), (self.vertices[i][0], self.vertices[i][0]), 5)
    def rotate_y(self):
        for i in range(len(self.vertices)):
            
            self.vertices[i] = convert_vector_to_int(camera_matrices.rotate_y(self.vertices[i], self.angle))
            # print(self.vertices[i])
        
        
