'''
    53. Write a Python program to create a list with infinite elements.
'''
import itertools
c = itertools.count(2,2)
for i in range(20):
    print(c)
    print(next(c))
