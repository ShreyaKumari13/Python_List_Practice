'''
    79. Write a Python program to remove the K'th element from a given list, print the new list.
    Original list:
    [1, 1, 2, 3, 4, 4, 5, 1]
    After removing an element at the kth position of the said list:
    [1, 1, 3, 4, 4, 5, 1]
'''
list1 = [1, 1, 2, 3, 4, 4, 5, 1]
n = int(input("Enter the nth index element: "))
list1.pop(n)
print(list1)

list1 = [1, 1, 2, 3, 4, 4, 5, 1]
n = int(input("Enter the nth according to length element: "))
list1.pop(n-1)
print(list1)

