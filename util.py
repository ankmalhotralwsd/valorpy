def get_matrix_mul_dim(a:list, b:list) -> list:
    return [len(a), len(b[0])]

def fill_with_zeros(x:int, y:int):
    c = []
    for i in range(x):
        c.append([])
        for j in range(y):
            c[i].append(0)
    return c

def dot(a:list, b:list) -> list:
    c = fill_with_zeros(len(a), len(b[0]))
    if len(a[0]) != len(b):
        print("ERROR - Can't Multiply These Dimensions")
        return c

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                c[i][j] += a[i][k] * b[k][j]
    return c

def weird_vector_to_matrix(a:list, b:list):
    c = fill_with_zeros(len(b), len(b[0]))
    for i in range(len(b)):
        for j in range(len(b[0])):
            c[i][j] = a[j] * b[i][j]
    return c

def vector_x_matrix(a:list, b:list, x, y):
    c = [0, 0, 0]
    print(a)
    # if len(a[0]) != len(b):
    #     print("ERROR - Can't Multiply These Dimensions")
    #     return c

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                c[i] += a[k] * b[k][j]
    print(c)
    return c

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