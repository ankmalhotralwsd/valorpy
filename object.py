from copy import deepcopy
import util
import mesh
import geometry
import numpy as np


class Object(geometry.Geometry):
    def __init__(self, x, y, z, x_s, y_s, z_s, mesh):
        super().__init__(x, y, z, x_s, y_s, z_s)
        self.mesh = mesh
        self.init_model_space_vertices()
    def init_model_space_vertices(self):
        self.colors = deepcopy(self.mesh.colors)
        self.model_space_faces = np.copy(self.mesh.faces)
        for i in range(len(self.model_space_faces)):
            self.model_space_faces[i] = util.weird_vector_to_matrix(self.scale, self.model_space_faces[i])
        
        self.faces = np.copy(self.model_space_faces)
        
    
        
        
