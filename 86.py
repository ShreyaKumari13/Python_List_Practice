'''
    86. Write a Python program to create a 3X3 grid with numbers.
    3X3 grid with numbers:
    [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
'''
list1 = []
for i in range(3):
    list1.append([])
    sum1 = 1
    for j in range(3):
        list1[i].append(sum1)
        sum1+=1
print(list1)

list1 = []
for i in range(3):
    list1.append([])
    for j in range(1,4):
        list1[i].append(j)
print(list1)