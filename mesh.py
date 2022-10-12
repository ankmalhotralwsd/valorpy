#ORDER OF VERTICES
#BACK TO FRONT
#BOTTOM LEFT TO TOP RIGHT

from tri import Tri
from obj_processing import return_faces_through_file


class Mesh:
    def __init__(self):
        self.faces = []


CUBE_MESH = Mesh()
CUBE_MESH.faces = return_faces_through_file("chicken.txt")





