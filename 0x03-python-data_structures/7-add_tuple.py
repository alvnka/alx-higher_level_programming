#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        tuple_a = (0, 0)
    elif len(tuple_b) == 0:
        tuple_b = (0, 0)
    elif len(tuple_a) < 2:
        if tuple_a[0] is None:
            tuple_a[0] = 0
        else:
            tuple_a = tuple_a + (0, )

    elif len(tuple_b) < 2:
        if tuple_b[0] is None:
            tuple_b[0] = 0
        else:
            tuple_b = tuple_b + (0, )

    element1 = tuple_a[0] + tuple_b[0]
    element2 = tuple_a[1] + tuple_b[1]
    new_tuple = (element1, element2)
    return (new_tuple)
