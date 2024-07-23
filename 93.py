'''
    93. Write a Python program to count the number of sublists contain a particular element.
    Original list:
    [[1, 3], [5, 7], [1, 11], [1, 15, 7]]
    Count 1 in the said list:
    3
    Count 7 in the said list:
    2
    Original list:
    [['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']]
    Count 'A' in the said list:
    3
    Count 'E' in the said list:
    1
'''
list1 = [[1, 3], [5, 7], [1, 11], [1, 15, 7]]
n = int(input("Enter the number: "))
count = 0
for i in list1:
    for j in i:
        if j==n:
            count+=1
print(count)

def counum(list1,n):
    count=0
    for i in list1:
        for j in i:
            if j==n:
                count+=1
    return count
list1 = [[1, 3], [5, 7], [1, 11], [1, 15, 7]]
n = int(input("Enter the number: "))
print(counum(list1,n))
n = int(input("Enter the number: "))
print(counum(list1,n))
n = int(input("Enter the number: "))
print(counum(list1,n))