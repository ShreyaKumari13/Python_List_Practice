'''
    9. Write a Python program to clone or copy a list.

'''

li1=[1,2,3,4,5]
li2=list(li1)
print("original list",li1)
print("new list",li2)

li1=[1,2,3,4,5]
li2=li1
print("original list",li1)
print("new list",li2)

li1=[1,2,3,4,5]
li2=li1.copy()
print("original list",li1)
print("new list",li2)

def Cloning(list1):
    list2=list1[:]
    return list2
list1=[1,2,3]
list2=Cloning(list1)
print(Cloning(list1))



