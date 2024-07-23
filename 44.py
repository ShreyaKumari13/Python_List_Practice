'''
    44. Write a Python program to generate groups of five consecutive numbers in a list.

'''
for i in range(5):
    for j in range(1,6):
        print(5*i + j,end=" ")



# l = [[5*i + j for j in range(1,6)] for i in range(5)]
# print(l)
