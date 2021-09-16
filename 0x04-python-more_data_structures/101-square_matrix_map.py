#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda elem_matx: list(map(lambda element: element**2,
                                               elem_matx)), matrix))
