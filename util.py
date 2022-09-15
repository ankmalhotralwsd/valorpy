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
