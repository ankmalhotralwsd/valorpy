import pygame
import util
import rotation_matrices
import camera

resolution = (1024, 576)
width = 3

class Line:
    def __init__(self, x, y, z, x2, y2, z2, color):
        self.world_pos = [x, y, z, 1]

        self.model_space_vertices = [[x, y, z, 1], [x2, y2, z2, 1]]
        self.world_space_vertices = list(self.model_space_vertices)
        self.projection_space_vertices = list(self.world_space_vertices)
        self.camera_space_vertices = list(self.projection_space_vertices)

        self.dot_size = 10 / resolution[1]
        self.color = color
    def draw(self, screen):
        self.world_space_vertices = list(self.model_space_vertices)
        self.camera_space_vertices = list(self.world_space_vertices)
        self.make_world_vertices()

        pygame.draw.circle(screen, (0, 255, 0), tuple(self.projection_space_vertices[0][:2]), 3)
        pygame.draw.circle(screen, (255, 0, 0), tuple(self.projection_space_vertices[1][:2]), 3)
        pygame.draw.line(screen, self.color, tuple(self.projection_space_vertices[0][:2]), tuple(self.projection_space_vertices[1][:2]), width)
    

    def make_world_vertices(self):
        for i in range(len(self.model_space_vertices)):

            self.translate_model_to_world_pos(i)

            self.world_space_vertices[i] = camera.Camera.convert_to_camera_space(self.world_space_vertices[i])
            

            self.convert_world_to_camera_space(i)
            self.convert_camera_space_to_perspective(i)
    

    def translate_model_to_world_pos(self , i):
        #world_space_vertices is already rotated thats why i translate that and not model_space_vertices
        self.world_space_vertices[i] = util.vector_plus_vector(self.world_space_vertices[i], self.world_pos, [3])

    #clip space
    def convert_camera_space_to_perspective(self, i):
        self.projection_space_vertices[i] = list(self.camera_space_vertices[i])
        self.projection_space_vertices[i] = camera.perspective_x_coords(self.projection_space_vertices[i])
        self.projection_space_vertices[i][0] = int(self.projection_space_vertices[i][0] / self.projection_space_vertices[i][3] * (resolution[1]))
        self.projection_space_vertices[i][1] = int(self.projection_space_vertices[i][1] / self.projection_space_vertices[i][3] * (resolution[0]))
        self.projection_space_vertices[i][2] = int(self.projection_space_vertices[i][2] / self.projection_space_vertices[i][3] * (resolution[1]))


        self.projection_space_vertices[i] = util.vector_plus_vector(self.projection_space_vertices[i], [resolution[0]/2, resolution[1]/2, 0, 0], [])
        self.projection_space_vertices[i][0] = int(self.projection_space_vertices[i][0])
        self.projection_space_vertices[i][1] = int(self.projection_space_vertices[i][1])
        self.projection_space_vertices[i][2] = int(self.projection_space_vertices[i][2])
        self.projection_space_vertices[i][3] = int(self.projection_space_vertices[i][3])

    def convert_world_to_camera_space(self, i):
        self.camera_space_vertices[i] = camera.world_x_coords(self.world_space_vertices[i])
        