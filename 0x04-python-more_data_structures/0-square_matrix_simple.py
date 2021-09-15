#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = [[element**2 for element in row] for row in matrix]
    return square

# Here are other ways solve the same problem:

# way 1: The most explicit
# square = []
# for row in matrix:
# ....row_list = []
# ....for element in row:
# ........row_list.append(element**2)
# ....square.append(row_list)
# return square

# way 2: Replacing row_list = [] in the way 1
# Where: row_list = [element**2 for element in row]
# Then:
# square = []
# for row in matrix:
# ....square.append([element**2 for element in row])
# return square

# way 3: Replacing row_list = [] in the way 1
# square = []
# for row in matrix:
# ....row_list = list(map(lambda element: element**2, row))
# ....square.append(row_list)
# return square
