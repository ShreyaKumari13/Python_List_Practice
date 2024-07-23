'''
    88. Write a Python program to read a square matrix from console and print the sum of matrix primary diagonal. 
    Accept the size of the square matrix and elements for each column separated with a space (for every row) as input from the user. 
    Input the size of the matrix: 3
    2 3 4
    4 5 6
    3 4 7
    Sum of matrix primary diagonal:
    14
'''
R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
matrix = []
for i in range(R):          # A for loop for row entries
    a =[]
    for j in range(C):
        b = int(input("Enter the elements: "))      # A for loop for column entries
        a.append(b)
    matrix.append(a)
# For printing the matrix
for i in range(R):
    for j in range(C):
        print(matrix[i][j], end = "  ")
    print()

# For addition in matrix
for j in range(C):
    sum1 = 0
    for i in range(R):
        sum1=sum1+matrix[i][j]
    print(sum1,end=' ')

# sum of matrix diagonally
print()
sum1 = 0
for i in range(R):
    for j in range(C):
        if (i==j):
            sum1=sum1+matrix[i][j]
print(sum1,end=' ')

