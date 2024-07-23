'''
    7. Write a Python program to remove duplicates from a list.
'''
list1 =[1,3,2,1]  
b=list(set(list1))
print(b)

list1 =[1,3,2,1]
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)  
