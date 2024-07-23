'''
    66. Write a Python program to find the list in a list of lists whose sum of elements is the highest.
    Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
    Expected Output: [10, 11, 12]
'''
# list1 = [[1,2,3],[10,11,12], [4,5,6], [7,8,9]]
# maxi=0
# for i in list1:
#     sum1=0
#     for j in i:
#         sum1+=j
#     print(sum1)
#     maxi = max(sum1, maxi)
# print("The highest sum of elements is:",maxi)

# def maximumSum(list1):
#     maxi = 0
#     for x in list1:
#         sum = 0 
#         for y in x:
#             sum+= y     
#         maxi = max(sum, maxi) 
#     return maxi
# list1 = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
# print(maximumSum(list1))

list1= [[1,2,3],[10,11,12], [4,5,6], [7,8,9]]
maxi=0
for i in list1:
    maxi = max(sum(i), maxi)
print(maxi)

def sumof(list1):
    maxi=0
    for i in list1:
        maxi=max(sum(i),maxi)
    return maxi
list1= [[1,2,3],[10,11,12], [4,5,6], [7,8,9]]
print(sumof(list1))



