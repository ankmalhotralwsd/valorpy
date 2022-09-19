import math
import util

resolution = (1024, 576)
aspect_ratio = resolution[1]/resolution[0]
field_of_view = 60
field_of_view_scaling_factor = math.degrees(math.tan(math.radians(field_of_view/2)))

zfar = 1000
znear = 1

bruh = (zfar/(zfar - znear)) - (zfar/(zfar - znear) * znear)

def perspective_x_coords(a):
    PERSPECTIVE_MATRIX = [[aspect_ratio * (1.0/field_of_view_scaling_factor), 0, 0, 0],
                            [0, 1.0/field_of_view_scaling_factor, 0, 0],
                            [0, 0, (zfar/(zfar - znear)), (-zfar/(zfar - znear))*znear],
                            [0, 0, 1, 0]]
    return util.matrix_x_vector(PERSPECTIVE_MATRIX, a)