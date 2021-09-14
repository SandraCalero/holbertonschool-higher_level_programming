#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    aux_tuple_a = list(tuple_a[0:2])
    aux_tuple_b = list(tuple_b[0:2])
    if len(tuple_a) == 0:
        aux_tuple_a = [0, 0]
    elif len(tuple_a) == 1:
        aux_tuple_a = [aux_tuple_a[0], 0]
    if len(tuple_b) == 0:
        aux_tuple_b = [0, 0]
    elif len(tuple_b) == 1:
        aux_tuple_b = [aux_tuple_b[0], 0]
    newtup = (aux_tuple_a[0] + aux_tuple_b[0], aux_tuple_a[1] + aux_tuple_b[1])
    return newtup
