'''
    64. Write a Python program to iterate over two lists simultaneously.
'''
num = [1, 2, 3]
color = ['red', 'white', 'black']
for i,j in zip(num,color):
    print(i,j)