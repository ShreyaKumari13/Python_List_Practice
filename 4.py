'''
    4. Write a Python program to get the smallest number from a list.

'''
a=[1,2,-8]
print(min(a))

def min_num_in_list( list ):
    min = 0
    for a in list:
        if a < min:
            min = a
    return min
print(min_num_in_list([1, 2, 10,-1,0]))