from copy import deepcopy
import pygame
import util
import rotation_matrices
import camera
import math
import random
import mesh

resolution = (1024, 576)
width = 1

class Geometry:
    def __init__(self, x, y, z, dim_x, dim_y, dim_z):
        self.world_pos = [x, y, z, 1]
        self.scale = [dim_x, dim_y, dim_z, 1]
        self.world_angle = [0, 0, 0]
        self.mesh = None



        self.model_space_tris = []
        self.world_space_tris = deepcopy(self.model_space_tris)
        self.projection_space_tris = deepcopy(self.world_space_tris)
        self.camera_space_tris = deepcopy(self.projection_space_tris)



        self.color = (random.randint(255//2, 255), random.randint(255//2, 255), random.randint(255//2, 255))
        self.dot_size = 10 / resolution[1]

    def rotate_y(self, angle , i):
        self.world_space_tris[i][0] = rotation_matrices.rotate_y(self.world_space_tris[i][0], angle)
        self.world_space_tris[i][1] = rotation_matrices.rotate_y(self.world_space_tris[i][1], angle)
        self.world_space_tris[i][2] = rotation_matrices.rotate_y(self.world_space_tris[i][2], angle)
    
    def rotate_z(self, angle , i):
        self.world_space_tris[i][0] = rotation_matrices.rotate_z(self.world_space_tris[i][0], angle)
        self.world_space_tris[i][1] = rotation_matrices.rotate_z(self.world_space_tris[i][1], angle)
        self.world_space_tris[i][2] = rotation_matrices.rotate_z(self.world_space_tris[i][2], angle)
    
    def rotate_x(self, angle, i):
        self.world_space_tris[i][0] = rotation_matrices.rotate_x(self.world_space_tris[i][0], angle)
        self.world_space_tris[i][1] = rotation_matrices.rotate_x(self.world_space_tris[i][1], angle)
        self.world_space_tris[i][2] = rotation_matrices.rotate_x(self.world_space_tris[i][2], angle)


    def draw(self, screen):
        self.world_space_tris = deepcopy(self.model_space_tris)
        self.camera_space_tris = deepcopy(self.world_space_tris)
        self.make_world_tris()

        for i in range(len(self.projection_space_tris)):
            pygame.draw.line(screen, self.color, tuple(self.projection_space_tris[i][0][:2]), tuple(self.projection_space_tris[i][1][:2]), width)
            pygame.draw.line(screen, self.color, tuple(self.projection_space_tris[i][1][:2]), tuple(self.projection_space_tris[i][2][:2]), width)
            pygame.draw.line(screen, self.color, tuple(self.projection_space_tris[i][2][:2]), tuple(self.projection_space_tris[i][0][:2]), width)

            

    def make_world_tris(self):
        for i in range(len(self.model_space_tris)):
            self.rotate_x(self.world_angle[0], i)
            self.rotate_y(self.world_angle[1], i)
            self.rotate_z(self.world_angle[2], i)

            self.translate_model_to_world_pos(i)
            
            for x in range(3):
                self.camera_space_tris[i][x] = camera.Camera.convert_to_camera_space(self.world_space_tris[i][x])
            
            self.convert_world_to_camera_space(i)
            self.convert_camera_space_to_perspective(i)
    

    def translate_model_to_world_pos(self , i):
        #world_space_tris is already rotated thats why i translate that and not model_space_tris
        self.world_space_tris[i][0] = util.vector_plus_vector(self.world_space_tris[i][0], self.world_pos, [3])
        self.world_space_tris[i][1] = util.vector_plus_vector(self.world_space_tris[i][1], self.world_pos, [3])
        self.world_space_tris[i][2] = util.vector_plus_vector(self.world_space_tris[i][2], self.world_pos, [3])
    
    
    def convert_camera_space_to_perspective(self, i):
        self.projection_space_tris[i] = deepcopy(self.camera_space_tris[i])

        for x in range(3):
            self.projection_space_tris[i][x] = camera.perspective_x_coords(self.projection_space_tris[i][x])
            #print(self.projection_space_tris[i][x])
            self.projection_space_tris[i][x][0] = int(self.projection_space_tris[i][x][0] / self.projection_space_tris[i][x][3] * (resolution[1]))
            self.projection_space_tris[i][x][1] = int(self.projection_space_tris[i][x][1] / self.projection_space_tris[i][x][3] * (resolution[0]))
            self.projection_space_tris[i][x][2] = int(self.projection_space_tris[i][x][2] / self.projection_space_tris[i][x][3] * (resolution[1]))
            self.projection_space_tris[i][x] = util.vector_plus_vector(self.projection_space_tris[i][x], [resolution[0]/2, resolution[1]/2, 0, 0], [])
            #print(self.projection_space_tris[i][x])

    def convert_world_to_camera_space(self, i):
        self.camera_space_tris[i][0] = util.rotate_around_origin(self.camera_space_tris[i][0], camera.Camera.world_angle)
        self.camera_space_tris[i][1] = util.rotate_around_origin(self.camera_space_tris[i][1], camera.Camera.world_angle)
        self.camera_space_tris[i][2] = util.rotate_around_origin(self.camera_space_tris[i][2], camera.Camera.world_angle)