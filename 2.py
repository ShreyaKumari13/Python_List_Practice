'''
    2. Write a Python program to multiplies all the items in a list.
'''
import numpy
a=[1,2,1]
b=numpy.product(a)
print(b)

import numpy
a=[1,2,-8]
b=numpy.prod(a)
print(b)

def multiply_list(items):
    tot = 1
    for x in items:
        tot *= x
    return tot
print(multiply_list([1,2,-8]))
