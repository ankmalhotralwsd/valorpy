from copy import deepcopy
import util
import mesh
import geometry


class Cube(geometry.Geometry):
    def __init__(self, x, y, z, x_s, y_s, z_s):
        super().__init__(x, y, z, x_s, y_s, z_s)
        self.init_model_space_vertices()
        
    def init_model_space_vertices(self):
        self.mesh = mesh.CUBE_MESH
        self.model_space_faces = list(self.mesh.faces)

        for i in range(len(self.model_space_faces)):
                self.model_space_faces[i] = util.weird_vector_to_matrix(self.scale, self.model_space_faces[i])

        self.world_space_faces = list(self.model_space_faces)
        self.projection_space_faces = list(self.world_space_faces)
    
        
        
