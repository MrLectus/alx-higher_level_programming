#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        return tuple_b
    if len(tuple_b) == 0:
        return tuple_a