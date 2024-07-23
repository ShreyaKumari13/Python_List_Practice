'''
    74. Write a Python program to pack consecutive duplicates of a given list elements into sublists.
    Original list: 
    [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
    After packing consecutive duplicates of the said list elements into sublists:
    [[0, 0], [1], [2], [3],[4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
'''
# x = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# list2=[]
# for i,v in enumerate(x):
#     if (v!=x[i-1]):
#         a = list2.append(v)
#         list(a)
# print(list2)

# x = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# list2 = []
# for i,v in enumerate(x):
#     list1 = []
#     list1 = x[i]
#     if x[i+1] == list1[0]:
#         list1.append(x[i+1])
#     else:
#         pass





from itertools import groupby
def pack(List):
    result = []
    for key,group in groupby(List):
         result.append(list(group))
    return result
l = [1, 1, 1, 2, 2, 3, 3, 4]
print(pack(l))