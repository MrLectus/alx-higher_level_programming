#!/usr/bin/python3
def add_tuple(tuple_a=(0,), tuple_b=(0,)):
    n = max(len(tuple_a), len(tuple_b))
    tuple_a = tuple_a + (0,) * (n - len(tuple_a))
    tuple_b = tuple_b + (0,) * (n - len(tuple_b))

    sum_tuple = tuple()

    for i in range(n):
        sum_tuple += (tuple_a[i] + tuple_b[i],)

    return sum_tuple
