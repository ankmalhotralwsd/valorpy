import math
import util
import geometry_matrices
import rotation_matrices

scale = [25, 25, 25]
vertices = util.weird_vector_to_matrix(scale, geometry_matrices.CUBE_VERTEX_MATRIX)
angle = 0

rotated_vertices = vertices

while True:
    angle += .0001
    for i in range(len(vertices)):
        rotated_vertices[i] = rotation_matrices.rotate_y(vertices[i], angle, 1, 3)
    print(rotated_vertices)