'''
    1. Write a Python program to sum all the items in a list.

'''
a=[1,2,-8]
b=sum(a)
print(b)

def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum_list([1,2,-8]))










