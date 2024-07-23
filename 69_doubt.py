'''
    69. Write a Python program to remove duplicates from a list of lists.
    Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
    New List : [[10, 20], [30, 56, 25], [33], [40]]
'''
# def remove(dupl):
#     list2=[]
#     for i in dupl:
#         for j in i:
#             if j not in list2:
#                 list2.append(j)
#     print(list2)
# dupl=[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# remove(dupl)

import itertools
num = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
num.sort()
new_num = list(num for num,_ in itertools.groupby(num))
print("New List", new_num)


