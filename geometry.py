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

        self.model_space_faces = []
        self.world_space_faces = deepcopy(self.model_space_faces)
        self.projection_space_faces = deepcopy(self.world_space_faces)
        self.camera_space_faces = deepcopy(self.projection_space_faces)
        self.xy_coords = deepcopy(self.projection_space_faces)

        self.faces = []

        self.color = (random.randint(255//2, 255), random.randint(255//2, 255), random.randint(255//2, 255))
        self.dot_size = 10 / resolution[1]

    def rotate_y(self, angle , i):
        for x in range(len(self.world_space_faces[i])):
            self.world_space_faces[i][x] = rotation_matrices.rotate_y(self.world_space_faces[i][x], angle)

    
    def rotate_z(self, angle , i):
        for x in range(len(self.world_space_faces[i])):
            self.world_space_faces[i][x] = rotation_matrices.rotate_z(self.world_space_faces[i][x], angle)
    
    def rotate_x(self, angle, i):
        for x in range(len(self.world_space_faces[i])):
            self.world_space_faces[i][x] = rotation_matrices.rotate_x(self.world_space_faces[i][x], angle)


    def draw(self, screen):
        self.world_space_faces = deepcopy(self.model_space_faces)
        self.camera_space_faces = deepcopy(self.world_space_faces)
        self.make_world_faces()

        
        # for i in range(len(self.projection_space_faces)):
        #     self.xy_coords = deepcopy(self.projection_space_faces)
        #     for x in range(len(self.projection_space_faces[i])):
        #         self.xy_coords[i][x] = self.projection_space_faces[i][x][:2]
        #     pygame.draw.polygon(screen, self.color, self.xy_coords[i])
        

        for i in range(len(self.projection_space_faces)):
            if len(self.projection_space_faces[i]) == 4:
                pygame.draw.line(screen, self.color, tuple(self.projection_space_faces[i][0][:2]), tuple(self.projection_space_faces[i][1][:2]), width)
                pygame.draw.line(screen, self.color, tuple(self.projection_space_faces[i][1][:2]), tuple(self.projection_space_faces[i][2][:2]), width)
                pygame.draw.line(screen, self.color, tuple(self.projection_space_faces[i][2][:2]), tuple(self.projection_space_faces[i][3][:2]), width)
                pygame.draw.line(screen, self.color, tuple(self.projection_space_faces[i][3][:2]), tuple(self.projection_space_faces[i][0][:2]), width)
            else:
                pygame.draw.line(screen, self.color, tuple(self.projection_space_faces[i][0][:2]), tuple(self.projection_space_faces[i][1][:2]), width)
                pygame.draw.line(screen, self.color, tuple(self.projection_space_faces[i][1][:2]), tuple(self.projection_space_faces[i][2][:2]), width)
                pygame.draw.line(screen, self.color, tuple(self.projection_space_faces[i][2][:2]), tuple(self.projection_space_faces[i][0][:2]), width)
            
        
            

    def make_world_faces(self):
        for i in range(len(self.model_space_faces)):
            self.rotate_x(self.world_angle[0], i)
            self.rotate_y(self.world_angle[1], i)
            self.rotate_z(self.world_angle[2], i)

            self.translate_model_to_world_pos(i)
            
            for x in range(len(self.camera_space_faces[i])):
                self.camera_space_faces[i][x] = camera.Camera.convert_to_camera_space(self.world_space_faces[i][x])
            
            self.convert_world_to_camera_space(i)
            self.convert_camera_space_to_perspective(i)
    

    def translate_model_to_world_pos(self , i):
        #world_space_faces is already rotated thats why i translate that and not model_space_faces
        for x in range(len(self.world_space_faces[i])):
            self.world_space_faces[i][x] = util.vector_plus_vector(self.world_space_faces[i][x], self.world_pos, [3])

    
    
    def convert_camera_space_to_perspective(self, i):
        self.projection_space_faces[i] = deepcopy(self.camera_space_faces[i])

        for x in range(len(self.projection_space_faces[i])):
            self.projection_space_faces[i][x] = camera.perspective_x_coords(self.projection_space_faces[i][x])

            self.projection_space_faces[i][x][0] = int(self.projection_space_faces[i][x][0] / self.projection_space_faces[i][x][3] * (resolution[1]))
            self.projection_space_faces[i][x][1] = int(self.projection_space_faces[i][x][1] / self.projection_space_faces[i][x][3] * (resolution[0]))
            self.projection_space_faces[i][x][2] = int(self.projection_space_faces[i][x][2] / self.projection_space_faces[i][x][3] * (resolution[1]))
            self.projection_space_faces[i][x] = util.vector_plus_vector(self.projection_space_faces[i][x], [resolution[0]/2, resolution[1]/2, 0, 0], [])


    def convert_world_to_camera_space(self, i):
        for x in range(len(self.camera_space_faces[i])):
            self.camera_space_faces[i][x] = util.rotate_around_origin(self.camera_space_faces[i][x], camera.Camera.world_angle)
