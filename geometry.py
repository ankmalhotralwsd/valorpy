import re
import pygame
import util
import rotation_matrices
import geometry_matrices
import camera
import math

resolution = (1024,576)

class Geometry:
    def __init__(self, x, y, z, dim_x, dim_y, dim_z):
        self.world_pos = [x, y, z, 1]
        self.scale = [dim_x, dim_y, dim_z, 1]
        self.world_angle = [0, 0, 0]
        self.model_space_vertices = []
        self.world_space_vertices = list(self.model_space_vertices)
        self.projection_space_vertices = list(self.world_space_vertices)

        self.dot_size = 10 / resolution[1]

    def rotate_y(self, angle , i):
        self.world_space_vertices[i] = rotation_matrices.rotate_y(self.world_space_vertices[i], angle)
    
    def rotate_z(self, angle , i):
        self.world_space_vertices[i] = rotation_matrices.rotate_z(self.world_space_vertices[i], angle) 
    
    def rotate_x(self, angle, i):
        self.world_space_vertices[i] = rotation_matrices.rotate_x(self.world_space_vertices[i], angle) 


    def draw(self, screen):
        self.world_space_vertices = list(self.model_space_vertices)
        self.make_world_vertices()

        for i in range(len(self.projection_space_vertices)):
            pygame.draw.circle(screen, (0, 0, 255), tuple(self.projection_space_vertices[i][:2]), 1000//self.projection_space_vertices[i][2])


    def make_world_vertices(self):
        for i in range(len(self.model_space_vertices)):
            self.rotate_x(self.world_angle[0], i)
            self.rotate_y(self.world_angle[1], i)
            self.rotate_z(self.world_angle[2], i)

            self.translate_model_to_world_pos(i)

            self.model_space_vertices[i] = camera.Camera.convert_to_camera_space(self.model_space_vertices[i])
            #self.convert_world_space_to_ortho_space(i)
            self.convert_world_space_to_perspective(i)
    

    def translate_model_to_world_pos(self , i):
        #world_space_vertices is already rotated thats why i translate that and not model_space_vertices
        self.world_space_vertices[i] = util.vector_plus_vector(self.world_space_vertices[i], self.world_pos, [3])


    #first need to convert to camera space but les not do that yet
    def convert_world_space_to_ortho_space(self, i):
        self.projection_space_vertices[i] = list(self.world_space_vertices[i])
        self.projection_space_vertices[i] = util.vector_plus_vector(self.world_space_vertices[i], [resolution[0]/2, resolution[1]/2, 0, 0], [])
    

    def convert_world_space_to_perspective(self, i):
        self.projection_space_vertices[i] = list(self.world_space_vertices[i])
        self.projection_space_vertices[i] = camera.perspective_x_coords(self.projection_space_vertices[i])
        self.projection_space_vertices[i][0] = int(self.projection_space_vertices[i][0] / self.projection_space_vertices[i][3] * (resolution[1]/2))
        self.projection_space_vertices[i][1] = int(self.projection_space_vertices[i][1] / self.projection_space_vertices[i][3] * (resolution[1]/2))
        self.projection_space_vertices[i][2] = int(self.projection_space_vertices[i][2] / self.projection_space_vertices[i][3] * (resolution[1]/2))


        self.projection_space_vertices[i] = util.vector_plus_vector(self.projection_space_vertices[i], [resolution[0]/2, resolution[1]/2, 0, 0], [])
        self.projection_space_vertices[i][0] = int(self.projection_space_vertices[i][0])
        self.projection_space_vertices[i][1] = int(self.projection_space_vertices[i][1])
        self.projection_space_vertices[i][2] = int(self.projection_space_vertices[i][2])
        self.projection_space_vertices[i][3] = int(self.projection_space_vertices[i][3])