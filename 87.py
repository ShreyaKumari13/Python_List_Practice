'''
    87. Write a Python program to read a matrix from console and print the sum for each column. Accept matrix rows, 
    columns and elements for each column separated with a space(for every row) as input from the user.
    Input rows: 2
    Input columns: 2
    Input number of elements in a row (1, 2, 3):
    1 2
    3 4
    sum for each column:
    4 6
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
        print(matrix[i][j], end = " ")
    print()

# For addition in matrix
for j in range(C):
    sum1 = 0
    for i in range(R):
        sum1=sum1+matrix[i][j]
    print(sum1,end=' ')


# rows = int(input("Input rows: "))
# columns = int(input("Input columns: "))
# matrix = [[0]*columns for row in range(rows)]
# print('Input number of elements in a row (1, 2, 3): ')
# for row in range(rows):
#     lines = list(map(int, input().split()))
#     for column in range(columns):
#         matrix[row][column] = lines[column]

# sum = [0]*columns
# print("sum for each column:")
# for column in range(columns):
#     for row in range(rows):
#         sum[column] += matrix[row][column]
#     print((sum[column]), ' ', end = '')



# list1 = [1,2,3,4,5,6,7,8,9]
# def great(num):
#     return num>5
# gr_than_5 = list(filter(great,list1))
# print(gr_than_5)

# from functools import reduce
# list1 = [1,2,3,4,5,6,7,8,9]
# gr_than_5 = reduce(lambda x,y:x+y,list1)
# print(gr_than_5)