'''
    90. Write a Python program to count number of lists in a given list of lists.
    Original list:
    [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
    Number of lists in said list of lists:
    4
    Original list:
    [[2, 4], [[6, 8], [4, 5, 8]], [10, 12, 14]]
    Number of lists in said list of lists:
    3
'''
list1 = [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
count = 0
for i in list1:
    if type(i)==list:
        count+=1
print(count)

