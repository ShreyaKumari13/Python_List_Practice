'''
    73. Write a Python program to remove consecutive duplicates of a given list.
    Original list:
    [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
    After removing consecutive duplicates:
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
'''
x = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
list2=[]
for i,v in enumerate(x):
    if ( v !=x[i-1]):
        list2.append(v)
print(list2)


from itertools import groupby
def compress(l_nums):
    return [key for key, group in groupby(l_nums)] 
n_list = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ]
print("\nAfter removing consecutive duplicates:")
print(compress(n_list)) 



