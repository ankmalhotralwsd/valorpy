import math
import util
import predefined_matrices
import camera_matrices

scale = [25, 25, 25]
vertices = util.weird_vector_to_matrix(scale, predefined_matrices.CUBE_VERTEX_MATRIX)
angle = 0

rotated_vertices = vertices

while True:
    angle += .0001
    for i in range(len(vertices)):
        rotated_vertices[i] = camera_matrices.rotate_y(vertices[i], angle, 1, 3)
    print(rotated_vertices)