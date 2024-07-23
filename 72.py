'''
    72. Write a Python program to flatten a given nested list structure.
    Original list: [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
    Flatten list:
    [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
'''
list1 = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
list2=[]
for i in list1:
    if type(i)==list:
        for j in i:
            list2.append(j)
    else:
        list2.append(i)
print(list2)