#ORDER OF VERTICES
#BACK TO FRONT
#BOTTOM LEFT TO TOP RIGHT
from obj_processing import return_faces_through_file
import random
import numpy as np

def get_avg_z(face):
    sum = 0
    for i in range(len(face)):
        sum += face[i][2]
    return sum / len(face)

class Mesh:
    def __init__(self, file_faces):
        self.faces, self.tris = file_faces



        self.colors = []
        for i in range(len(self.faces)):
            self.colors.append((random.randint(255//10, 255), random.randint(255//10, 255), random.randint(255//10, 255)))
    def sort_face_indices(self):
        pass
    def angle_of_face(self) -> int:
        pass



CUBE_MESH = Mesh(return_faces_through_file("cube.txt"))
CHICKEN_MESH = Mesh(return_faces_through_file("chicken.txt"))






