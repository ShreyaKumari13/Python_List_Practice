'''
    29. Write a Python program to get unique values from a list.

'''
my_list = [10, 20, 30, 40, 20, 50, 60, 40]
print("Original List : ",my_list)
my_set = list(set(my_list))
print("List of unique numbers : ",my_set)
