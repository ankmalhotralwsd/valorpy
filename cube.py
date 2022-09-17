import pygame
from util import weird_vector_to_matrix
from util import convert_vector_to_int
from predefined_matrices import CUBE_VERTEX_MATRIX
import camera_matrices
from geometry import Geometry

class Cube(Geometry):
    def __init__(self, x, y, z, x_s, y_s, z_s):
        super().__init__(x, y, z, x_s, y_s, z_s)
        self.init_model_space_vertices()
    def init_model_space_vertices(self):
        self.model_space_vertices = weird_vector_to_matrix(self.scale, CUBE_VERTEX_MATRIX)
        self.world_space_vertices = list(self.model_space_vertices)
        self.projection_space_vertices = list(self.world_space_vertices)



    
        
        
