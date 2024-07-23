'''
    23. Write a Python program to flatten a shallow list.
'''

import itertools
original_list = [[2,4,3],[1,5,6], [9], [7,9,0]]
new_merged_list = list(itertools.chain(*original_list))
print(new_merged_list)


a = [[2,4,3],[1,5,6], 5,6,7,[9], [7,9,0]]
b=[]
for i in a:
    if type(i)==list:
        for j in i:
            b.append(j)
print(b)

# a=[[1,2],5,[3,3],7,8,[9,10]]
# c=[]
# for i in a:
#     try:
#         for j in i:
#             c.append(j)
#     except:
#         pass
# print(c)

# a=[[1,2],5,[3,3],7,8,[9,10]]
# c=[]
# for i in a:
#     try:
#         if len(i)>1:
#             c.append(i)
#     except:
#         pass
# print(c)