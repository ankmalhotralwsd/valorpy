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
        self.model_space_tris = list(self.mesh.tris)

        for i in range(len(self.model_space_tris)):
                self.model_space_tris[i] = util.weird_vector_to_matrix(self.scale, self.model_space_tris[i])

        self.world_space_tris = list(self.model_space_tris)
        self.projection_space_tris = list(self.world_space_tris)

        print(self.projection_space_tris)
    
        
        
