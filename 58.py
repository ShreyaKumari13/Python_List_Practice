'''
    58. Write a Python program to replace the last element in a list with another list.
    Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
    Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]
'''
list1 = [1, 3, 5, 7, 9, 10] 
list2 = [2, 4, 6, 8]
list1.pop()
list3=list1+list2
print(list3)

num1 = [1, 3, 5, 7, 9, 10]
num2 = [2, 4, 6, 8]
num1[-1:] = num2
print(num1)
