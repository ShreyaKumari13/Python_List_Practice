'''
    81. Write a Python program to extract a given number of randomly selected elements from a given list.
    Original list:
    [1, 1, 2, 3, 4, 4, 5, 1]
    Selected 3 random numbers of the above list:
    [4, 4, 1]
'''
import random
list1 = [1, 1, 2, 3, 4, 4, 5, 1]
list2 = []
for i in range(3):
    b = random.choice(list1)
    list2.append(b)
print(list2)


list1 = [1, 1, 2, 3, 4, 4, 5, 1]
d = random.sample(list1,3)
print(d)

def seleran(list1,n):
    return random.sample(list1,n)
list1 = [1, 1, 2, 3, 4, 4, 5, 1]
n = int(input("Enter the number of elements: "))
print(seleran(list1,n))