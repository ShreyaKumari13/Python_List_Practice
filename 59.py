'''
    59. Write a Python program to check whether the n-th element exists in a given list.
'''
list1=[1,2,3,4,5,6,7,8,9]
n=int(input("enter the number: "))
for i in list1:
    if n==i:
        print("exist")
    else:
        print("doesn't exist")