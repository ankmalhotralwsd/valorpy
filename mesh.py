#ORDER OF VERTICES
#BACK TO FRONT
#BOTTOM LEFT TO TOP RIGHT

from triface import Tri

CV = [[-1, -1, -1, 1], #back
                    [1, -1, -1, 1],
                    [-1, 1, -1, 1],
                    [1, 1, -1, 1],
                    #front
                    [-1, -1, 1, 1],
                    [1, -1, 1, 1],
                    [-1, 1, 1, 1],
                    [1, 1, 1, 1]]


class Mesh:
    def __init__(self):
        self.tris = []


CUBE_MESH = Mesh()

CUBE_MESH.tris.append([CV[0], CV[1], CV[2]])
CUBE_MESH.tris.append([CV[1], CV[2], CV[3]])

CUBE_MESH.tris.append([CV[4], CV[5], CV[6]])
CUBE_MESH.tris.append([CV[5], CV[6], CV[7]])


