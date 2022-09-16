import math
import util



def rotate_y(vertex, angle):
    rotation_matrix = [[(math.cos(angle)), 0, (math.sin(angle))],
                        [0, 1, 0],
                        [(-math.sin(angle)), 0, (math.cos(angle))]]
    return util.vector_x_matrix(vertex, rotation_matrix, 1, 3)