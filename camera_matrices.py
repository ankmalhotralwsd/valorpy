import math
import util


def rotate_y(vertex, angle, x, y):
    rotation_matrix = [[math.cos(angle), 0, math.sin(angle)],
                        [0, 1, 0],
                        [-math.sin(angle), 0, math.cos(angle)]]
    # print(util.matrix_x_vector(rotation_matrix, vertex, x, y))
    return util.matrix_x_vector(rotation_matrix, vertex, x, y)

def rotate_z(vertex, angle, x, y):
    rotation_matrix = [[math.cos(angle), -math.sin(angle), 0],
                        [math.sin(angle), math.cos(angle), 0],
                        [0, 0, 1]]
    # print(util.matrix_x_vector(rotation_matrix, vertex, x, y))
    return util.matrix_x_vector(rotation_matrix, vertex, x, y)

def rotate_x(vertex, angle, x, y):
    rotation_matrix = [[1, 0, 0],
                        [0, math.cos(angle), -math.sin(angle)],
                        [0, math.sin(angle), math.cos(angle)]]
    return util.matrix_x_vector(rotation_matrix, vertex, 1, 3)

