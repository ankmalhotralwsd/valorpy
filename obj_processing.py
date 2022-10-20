import re
import numpy as np

def return_faces_through_file(file):
    vertices = []
    face_indices = []
    faces = []

    
    quads = []
    tris = []
    quad_indices = []
    tri_indices = []

    in_file = open(file)
    line = in_file.readline()
    
    line_num = 1

    while(line):
        l = re.split(r" +", line)
        if l[0] == "v":
            vertices.append([float(l[1]), float(l[2]), float(l[3]), 1])
        elif l[0] == "f":
            if len(l)==5:
                quad_indices.append([int(l[1].split("/")[0])-1, int(l[2].split("/")[0])-1, int(l[3].split("/")[0])-1, int(l[4].split("/")[0])-1])
            else:
                tri_indices.append([int(l[1].split("/")[0])-1, int(l[2].split("/")[0])-1, int(l[3].split("/")[0])-1])
        line = in_file.readline()
        line_num += 1


    for i in range(len(quad_indices)):
        quad = []
        if len(quad_indices[i]) == 4:
            quad = [vertices[quad_indices[i][0]], vertices[quad_indices[i][1]], vertices[quad_indices[i][2]], vertices[quad_indices[i][3]]]
        quads.append(quad)

    for i in range(len(tri_indices)):
        tri = []
        if len(tri_indices[i]) == 3:
            tri = [vertices[tri_indices[i][0]], vertices[tri_indices[i][1]], vertices[tri_indices[i][2]]]
        tris.append(tri)

    return np.array(quads, dtype=np.float64), np.array(tris, dtype=np.float64)
