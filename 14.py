'''
    14. Write a Python program to print the numbers of a specified list after removing even numbers from it.

'''
num=[1,2,3,4,5,6]
num2=[]
for i in num:
    if i%2==0:
        num.remove(i)
print(num)

num = [7,8, 120, 25, 44, 20, 27]
num = [x for x in num if x%2!=0]
print(num)
