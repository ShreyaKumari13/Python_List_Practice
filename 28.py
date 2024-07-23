'''
    28. Write a Python program to find the second largest number in a list.

'''
list1=[]
for i in range(5):
    a=int(input("Enter the number: "))
    list1.append(a)
list1.sort()
print("The second smallest number is: ",list1[-2])