'''
    12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
    Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    Expected Output : ['Green', 'White', 'Black']
'''
# color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
# print(color)

# color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# for index,i in enumerate(color):
#     if index not in (0,4,5):
#         color.pop(index)
# print(color)



l=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

del l[0]
print(l)
del l[-1]
print(l)
del l[6]
print(l)

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
for index,i in enumerate(color):
    if (index==0):
        color.pop(index)
    print(color)