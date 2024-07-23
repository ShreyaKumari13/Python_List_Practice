'''
    3. Write a Python program to get the largest number from a list.
'''
a=[1,2,-8]
print(max(a))

def max_num_in_list( list ):
    max = 0
    for a in list:
        if a > max:
            max = a
    return max
print(max_num_in_list([1, 2, 10, 0]))

