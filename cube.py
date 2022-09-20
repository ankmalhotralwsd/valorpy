import util
import geometry_matrices
import geometry


class Cube(geometry.Geometry):
    def __init__(self, x, y, z, x_s, y_s, z_s):
        super().__init__(x, y, z, x_s, y_s, z_s)
        self.init_model_space_vertices()
        
    def init_model_space_vertices(self):
        self.model_space_vertices = util.weird_vector_to_matrix(self.scale, geometry_matrices.CUBE_VERTEX_MATRIX)
        self.world_space_vertices = list(self.model_space_vertices)
        self.projection_space_vertices = list(self.world_space_vertices)


    
        
        
