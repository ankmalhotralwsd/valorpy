from this import s
import pygame
import util
import rotation_matrices
import camera
import math

resolution = (1024, 576)
width = 1

class Geometry:
    def __init__(self, x, y, z, dim_x, dim_y, dim_z):
        self.world_pos = [x, y, z, 1]
        self.scale = [dim_x, dim_y, dim_z, 1]
        self.world_angle = [0, 0, 0]
        self.model_space_vertices = []
        self.world_space_vertices = list(self.model_space_vertices)
        self.projection_space_vertices = list(self.world_space_vertices)
        self.camera_space_vertices = list(self.projection_space_vertices)

        self.dot_size = 10 / resolution[1]

    def rotate_y(self, angle , i):
        self.world_space_vertices[i] = rotation_matrices.rotate_y(self.world_space_vertices[i], angle)
    
    def rotate_z(self, angle , i):
        self.world_space_vertices[i] = rotation_matrices.rotate_z(self.world_space_vertices[i], angle) 
    
    def rotate_x(self, angle, i):
        self.world_space_vertices[i] = rotation_matrices.rotate_x(self.world_space_vertices[i], angle) 


    def draw(self, screen):
        self.world_space_vertices = list(self.model_space_vertices)
        self.camera_space_vertices = list(self.world_space_vertices)
        self.make_world_vertices()

        for i in range(len(self.projection_space_vertices)):
            for j in range(len(self.projection_space_vertices)):
                pygame.draw.line(screen, (0, 0, 255), tuple(self.projection_space_vertices[i][:2]), tuple(self.projection_space_vertices[j][:2]), width)
    

    def make_world_vertices(self):
        for i in range(len(self.model_space_vertices)):
            self.rotate_x(self.world_angle[0], i)
            self.rotate_y(self.world_angle[1], i)
            self.rotate_z(self.world_angle[2], i)

            # self.rotate_x(math.radians(camera.Camera.world_angle[0]), i)
            # self.rotate_y(math.radians(camera.Camera.world_angle[1]), i)

            self.translate_model_to_world_pos(i)

            
           
            self.camera_space_vertices[i] = camera.Camera.convert_to_camera_space(self.world_space_vertices[i])
            self.convert_world_to_camera_space(i)

            

            self.convert_camera_space_to_perspective(i)
    

    def translate_model_to_world_pos(self , i):
        #world_space_vertices is already rotated thats why i translate that and not model_space_vertices
        self.world_space_vertices[i] = util.vector_plus_vector(self.world_space_vertices[i], self.world_pos, [3])


    #clip space
    def convert_camera_space_to_ortho_space(self, i):
        self.projection_space_vertices[i] = list(self.world_space_vertices[i])
        self.projection_space_vertices[i] = util.vector_plus_vector(self.world_space_vertices[i], [resolution[0]/2, resolution[1]/2, 0, 0], [])
    
    #clip space
    def convert_camera_space_to_perspective(self, i):
        self.projection_space_vertices[i] = list(self.camera_space_vertices[i])
        self.projection_space_vertices[i] = camera.perspective_x_coords(self.projection_space_vertices[i])
        self.projection_space_vertices[i][0] = int(self.projection_space_vertices[i][0] / self.projection_space_vertices[i][3] * (resolution[1]))
        self.projection_space_vertices[i][1] = int(self.projection_space_vertices[i][1] / self.projection_space_vertices[i][3] * (resolution[0]))
        self.projection_space_vertices[i][2] = int(self.projection_space_vertices[i][2] / self.projection_space_vertices[i][3] * (resolution[1]))


        self.projection_space_vertices[i] = util.vector_plus_vector(self.projection_space_vertices[i], [resolution[0]/2, resolution[1]/2, 0, 0], [])

    def convert_world_to_camera_space(self, i):
        self.camera_space_vertices[i] = camera.world_x_coords(self.world_space_vertices[i])
        self.camera_space_vertices[i] = util.rotate_around_origin(self.camera_space_vertices[i], camera.Camera.world_angle)
        # self.camera_space_vertices[i] = rotation_matrices.rotate_x(self.camera_space_vertices[i], math.radians(camera.Camera.world_angle[0]))
        # self.camera_space_vertices[i] = rotation_matrices.rotate_y(self.camera_space_vertices[i], math.radians(camera.Camera.world_angle[1]))