'''
    80. Write a Python program to insert an element at a specified position into a given list.
    Original list:
    [1, 1, 2, 3, 4, 4, 5, 1]
    After inserting an element at kth position in the said list:
    [1, 1, 12, 2, 3, 4, 4, 5, 1]
'''
# list1 = [1, 1, 2, 3, 4, 4, 5, 1]
# ind = int(input("Enter the index: "))
# ele = int(input("Enter the elements: "))
# list1.insert(ind,ele)
# print(list1)

def insertele(ind,ele):
    return list1.insert(ind,ele)
list1 = [1, 1, 2, 3, 4, 4, 5, 1]
ind = int(input("Enter the index: "))
ele = int(input("Enter the elements: "))
insertele(ind,ele)
print(list1)

