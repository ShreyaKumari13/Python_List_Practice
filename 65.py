'''
    65. Write a Python program to move all zero digits to end of a given list of numbers.
    Expected output:
    Original list:
    [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
    Move all zero digits to end of the said list of numbers:
    [3, 4, 6, 2, 6, 7, 6, 9, 10, 7, 4, 4, 5, 3, 2, 9, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
'''
list1=[3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
list2=[]
list3=[]
for i in list1:
    if i!=0:
        list2.append(i)
    else:
        list3.append(i)
print(list2+list3)
