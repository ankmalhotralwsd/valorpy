import re

def return_faces_through_file(file):
    vertices = []
    face_indices = []
    faces = []


    in_file = open(file)
    line = in_file.readline()
    
    while(line):
        l = re.split(" ", line)
        
        if l[0] == "v":
            vertices.append([float(l[1]), float(l[2]), float(l[3]), 1])
        elif l[0] == "f":
            
            if len(l)==5:
                face_indices.append([int(l[1].split("/")[0])-1, int(l[2].split("/")[0])-1, int(l[3].split("/")[0])-1, int(l[4].split("/")[0])-1])
            else:
                face_indices.append([int(l[1].split("/")[0])-1, int(l[2].split("/")[0])-1, int(l[3].split("/")[0])-1])
        else:
            break
        line = in_file.readline()

    for i in range(len(face_indices)):
        face = []
        if len(face_indices[i]) == 4:
            face = [vertices[face_indices[i][0]], vertices[face_indices[i][1]], vertices[face_indices[i][2]], vertices[face_indices[i][3]]]
        else:
            face = [vertices[face_indices[i][0]], vertices[face_indices[i][1]], vertices[face_indices[i][2]]]

        faces.append(face)


    return faces
