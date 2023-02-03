#!/usr/bin/python3
# adding two tuples 
def add_tuple(tuple_a=(), tuple_b=()):
    i, j = len(tuple_a), len(tuple_b)
    return ((tuple_a[0] if i >= 1 else 0) + (tuple_b[0] if j >= 1 else 0), (tuple_a[1] if i >= 2 else 0) + (tuple_b[1] if j >= 2 else 0))
    

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))
