'''
    39. Write a Python program to convert a list of multiple integers into a single integer.
    Sample list: [11, 33, 50]
    Expected Output: 113350
'''

L = [11, 33, 50]
print("Original List: ",L)
x = int("".join(map(str, L)))
print("Single Integer: ",x)