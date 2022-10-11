#ORDER OF VERTICES
#BACK TO FRONT
#BOTTOM LEFT TO TOP RIGHT

from triface import Tri

CV = [[-1, -1, -1, 1], #back
                    [1, -1, -1, 1],
                    [-1, 1, -1, 1],
                    [1, 1, -1, 1],
                    #fron
                    [-1, -1, 1, 1],
                    [1, -1, 1, 1],
                    [-1, 1, 1, 1],
                    [1, 1, 1, 1]]


class Mesh:
    def __init__(self):
        self.tris = []


CUBE_MESH = Mesh()
CUBE_MESH.tris.append(Tri(CV[0], CV[1], CV[2]))
CUBE_MESH.tris.append(Tri(CV[0], CV[1], CV[2]))



