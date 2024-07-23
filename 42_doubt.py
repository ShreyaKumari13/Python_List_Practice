'''
    42. Write a Python program to find missing and additional values in two lists.
    Sample data : Missing values in second list: b,a,c
    Additional values in second list: g,h
'''
list1 = ['a','b','c','d','e','f']
list2 = ['d','e','f','g','h']
print('Missing values in second list: ', ','.join(set(list1).difference(list2)))
print('Additional values in second list: ', ','.join(set(list2).difference(list1)))


list1 = ['a','b','c','d','e','f']
list2 = ['d','e','f','g','h']
list3=[]
for i in list1:
    for j in list2:
        if i==j:
            list3.append(j)
print(list3)