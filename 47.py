'''
    47. Write a Python program to insert an element before each element of a list.
'''
list1=[1,2,3,4]
list2=[]
for i in list1:
    list2.append(5)
    list2.append(i)
print(list2)


color = ['Red', 'Green', 'Black']
color2=[]
for i in color:
    for j in ("c",i):
        color2.append(j)
print(color2)
