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

        self.colors = deepcopy(self.mesh.colors)
        self.model_space_faces = deepcopy(self.mesh.faces)
        for i in range(len(self.model_space_faces)):
            self.model_space_faces[i] = util.weird_vector_to_matrix(self.scale, self.model_space_faces[i])
        
        self.faces = deepcopy(self.model_space_faces)
        
    
        
        
