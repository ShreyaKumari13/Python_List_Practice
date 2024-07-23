'''
    22. Write a Python program to find the index of an item in a specified list.
'''
list1=["A","B","C","D","E"]
a=input("Enter the string: ")
for index,i in enumerate(list1):
    if i==a:
        print(index) 

num =[10, 30, 4, -6]
print(num.index(30))
