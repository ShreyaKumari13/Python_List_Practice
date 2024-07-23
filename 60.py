'''
    60. Write a Python program to find a tuple, the smallest second index value from a list of tuples. 

'''
x = [(4, 6), (1, 2), (6, 3)]
mini=x[0][1]
for i in x:
    if i[1]<mini:
        mini=i[1]
print(mini)