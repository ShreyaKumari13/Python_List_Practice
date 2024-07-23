'''
    11. Write a Python function that takes two lists and returns 
        True if they have at least one common member.
'''
list1=[1,2,3]
list2=[4,3,5]
for i in list1:
    for j in list2:
        if i==j:
            result=True
print(result)

list1=[1,2,3,4,5] 
list2=[5,6,7,8,9]
result = False
for x in list1:
    for y in list2:
        if x == y:
            result = True
print(result)















