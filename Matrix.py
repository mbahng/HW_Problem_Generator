import numpy as np
standard_elements = np.arange(-12, 12.5, 0.5)
stand_elem_dist = np.array([.5, .1, .5, .2, .6, .3, 3, 1, 3, 1, 3, 1, 4, 1, 4, 1, 4, 1, 5, 2, 5, 3, 5, 3, 4, 3, 5, 3, 5, 2, 5, 1, 4, 1,
4, 1, 4, 1, 3, 1, 3, 1, 3, .3, .6, .2, .5, .1, .5], dtype="float32")
stand_elem_dist /= np.sum(stand_elem_dist)

standard_scalars = np.arange(-8, 10, 1)
stand_scalar_dist = np.array([1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 3, 3, 3, 2, 2, 2, 1, 1], dtype="float32")
stand_scalar_dist /= np.sum(stand_scalar_dist)

simple_elem = np.arange(-5, 6, 1)
simple_dist = np.array([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1], dtype="float32")
simple_dist /= np.sum(simple_dist)

matrix_size = np.array([1, 2, 3, 4])
matrix_size_dist = np.array([0.15, 0.4, 0.35, 0.1])

def ConstructMatrix(n, m, simple=False):
    if simple==False:
        matrix = "\\begin{pmatrix} "
        for i in range(n):
            row = ""
            for j in range(m):
                row += f"{np.random.choice(standard_elements, p=stand_elem_dist)} & "
            row = row[:-2] + "\\\\"
            matrix += row
        matrix = matrix[:-3] + " \\end{pmatrix}"
        return matrix
    else:
        matrix = "\\begin{pmatrix} "
        for i in range(n):
            row = ""
            for j in range(m):
                row += f"{np.random.choice(simple_elem, p=simple_dist)} & "
            row = row[:-2] + "\\\\"
            matrix += row
        matrix = matrix[:-3] + " \\end{pmatrix}"
        return matrix

def ConstructVector(k, simple=False):
    if simple==False:
        return ConstructMatrix(k, 1, simple=False)
    else:
        return ConstructMatrix(k, 1, simple=True)

def VectorDotProduct(k, simple=False):
    if simple==False:
        vector1 = ConstructVector(k, simple=False)
        vector2 = ConstructVector(k, simple=False)
    else:
        vector1 = ConstructVector(k, simple=True)
        vector2 = ConstructVector(k, simple=True)
    string = vector1 + " \cdot " + vector2
    return f'''\\begin{{definition}} Compute the dot product. \n \[{string}\] \n \\end{{definition}}'''


def MatrixMultiplication(n, m, p, simple=False):
    if simple==False:
        matrix1 = ConstructMatrix(n, m, simple=False)
        matrix2 = ConstructMatrix(m, p, simple=False)
    else:
        matrix1 = ConstructMatrix(n, m, simple=True)
        matrix2 = ConstructMatrix(m, p, simple=True)
    string = matrix1 + "\; " + matrix2
    return f'''\\begin{{definition}} Multiply the matrices. \n \[{string}\] \n \\end{{definition}}'''

def VectorLinComb(dim, no):
    string = ""
    for i in range(no):
        scalar = np.random.choice(standard_scalars, p=stand_scalar_dist)
        while scalar == 0:
            scalar = np.random.choice(standard_scalars, p=stand_scalar_dist)
        if scalar < 0:
            scalar = f"({scalar})"
        vector = ConstructVector(dim)
        string += f"{scalar} \, {vector} + "
    string = f"{string[:-3]}"
    return f'''\\begin{{definition}} Compute the sum of vectors. \n \[{string}\] \n \\end{{definition}}'''

def MatrixLinComb(n, m, no):
    string = ""
    for i in range(no):
        scalar = np.random.choice(standard_scalars, p=stand_scalar_dist)
        while scalar == 0:
            scalar = np.random.choice(standard_scalars, p=stand_scalar_dist)
        if scalar < 0:
            scalar = f"({scalar})"
        matrix = ConstructMatrix(n, m)
        string += f"{scalar} \, {matrix} + "
    string = f"{string[:-3]}"
    return f'''\\begin{{definition}} Compute the sum of matrices. \n \[{string}\] \n \\end{{definition}}'''

def VectorCrossProduct():
    vector1 = ConstructVector(3, simple=True)
    vector2 = ConstructVector(3, simple=True)
    string = vector1 + " \\times " + vector2
    return f'''\\begin{{definition}} Compute the cross product. \n \[{string}\] \n \\end{{definition}}'''


if __name__ == "__main__":
    for i in range (10):
        n = p = np.random.choice(matrix_size, p=matrix_size_dist)
        m = np.random.choice(matrix_size, p=matrix_size_dist)
        while n == 4 and p == 4:
            n = p = np.random.randint(2, 4)
        print(MatrixMultiplication(n, m, p, simple=True))

