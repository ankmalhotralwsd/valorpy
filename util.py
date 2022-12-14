import math
import rotation_matrices
import numpy as np

def get_matrix_mul_dim(a:list, b:list) -> list:
    return [len(a), len(b[0])]


def fill_with_zeros(x:int, y:int):
    c = []
    for i in range(x):
        c.append([])
        for j in range(y):
            c[i].append(0)
    return c

def fill_vector_zero(x):
    c = []
    for i in range(x):
        c.append(0)
    return c


def weird_vector_to_matrix(a:list, b:list):
    c = fill_with_zeros(len(b), len(b[0]))
    for i in range(len(b)):
        for j in range(len(b[0])):
            c[i][j] = a[j] * b[i][j]
    return c


def matrix_x_vector(a, b):
    # c = fill_vector_zero(len(a))

    # for i in range(len(a)):
    #     for k in range(len(b)):
    #         c[i] += a[i][k] * b[k]
    # return c
    return np.dot(a, b)
    


def convert_matrix_to_int(a:list):
    for i in range(len(a)):
        for j in range(len(a[0])):
            a[i][j] = int(a[i][j])


def convert_vector_to_int(a:list):
    c = list(range(len(a)))
    for i in range(len(a)):
        c[i] = int(a[i])
    # print (c)
    return c


def vector_plus_vector(a:list, b:list, indices_to_skip:list):
    c = list(range(len(a)))
    if len(a) != len(b):
        return

    for i in range(len(a)):
        if i not in indices_to_skip:
            c[i] = a[i] + b[i]
        else:
            c[i] = a[i]

    return c

def vector_minus_vector(a:list, b:list, indices_to_skip:list):
    c = list(range(len(a)))
    if len(a) != len(b):
        return

    for i in range(len(a)):
        if i not in indices_to_skip:
            c[i] = a[i] - b[i]
        else:
            c[i] = a[i]

    return c


def vector_x_scalar(a, b, exclude):
    c = list(range(len(a)))
    for i in range(len(a)):
        if i not in exclude:
            c[i] = a[i] * b
    return c


def get_magnitude_of_vector(a):
    return math.sqrt(a[0]*a[0] + a[1]*a[1] + a[2]*a[2])


def normalize_vector(a):
    magnitude = get_magnitude_of_vector(a)
    return [a[0]/magnitude, a[1]/magnitude, a[2]/magnitude, 1]


def rotate_around_origin(a, angle):
    camera_to_point = a
    normalized = normalize_vector(camera_to_point)
    magnitude = get_magnitude_of_vector(camera_to_point)
    
    normalized = rotation_matrices.rotate_y(normalized, math.radians(angle[1]))
    normalized = rotation_matrices.rotate_x(normalized, math.radians(angle[0]))
    
    

    vector = vector_x_scalar(normalized, magnitude, [3])
    return vector