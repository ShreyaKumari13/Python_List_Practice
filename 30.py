'''
    30. Write a Python program to get the frequency of the elements in a list.

'''
my_list = [10, 20, 30, 40, 20, 50, 60, 40]
print(my_list.count(20))

import collections
my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
print("Original List : ",my_list)
ctr = collections.Counter(my_list)
print("Frequency of the elements in the List : ",ctr)

