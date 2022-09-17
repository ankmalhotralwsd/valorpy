import pygame
import util
import camera_matrices
import predefined_matrices

class Geometry:
    def __init__(self, x, y, z, dim_x, dim_y, dim_z):
        self.world_pos = [x, y, z]
        self.scale = [dim_x, dim_y, dim_z]
        self.world_angle = [0, 0, 0]
        self.model_space_vertices = []
        self.world_space_vertices = list(self.model_space_vertices)
        self.projection_space_vertices = list(self.world_space_vertices)

    def rotate_y(self, angle , i):
        self.world_space_vertices[i] = camera_matrices.rotate_y(self.world_space_vertices[i], angle, 1, 3)
    def rotate_z(self, angle , i):
        self.world_space_vertices[i] = camera_matrices.rotate_z(self.world_space_vertices[i], angle, 1, 3) 
    def rotate_x(self, angle, i):
        self.world_space_vertices[i] = camera_matrices.rotate_x(self.world_space_vertices[i], angle, 1, 3) 

    def draw(self, screen):
        self.world_space_vertices = list(self.model_space_vertices)
        self.make_world_vertices()
        
        #pygame.draw.lines(screen, (255, 255, 255), True, self.projection_space_vertices, width=5)
        # print(self.projection_space_vertices)
        for i in range(len(self.projection_space_vertices)):
            pygame.draw.circle(screen, (0, 0, 255), tuple(self.projection_space_vertices[i]), 5)
    def make_world_vertices(self):
        for i in range(len(self.model_space_vertices)):
            self.rotate_x(self.world_angle[0], i)
            self.rotate_y(self.world_angle[1], i)
            self.rotate_z(self.world_angle[2], i)

            self.translate_model_to_world_pos(i)
            self.convert_world_space_to_projection_space(i)
    
    def translate_model_to_world_pos(self , i):
        #world_space_vertices is already rotated thats why i translate that and not model_space_vertices
        self.world_space_vertices[i] = util.vector_plus_vector(self.world_space_vertices[i], self.world_pos)

    #first need to convert to camera space but les not do that yet
    def convert_world_space_to_projection_space(self, i):
        self.projection_space_vertices[i] = [self.world_space_vertices[i][0], self.world_space_vertices[i][1]]
