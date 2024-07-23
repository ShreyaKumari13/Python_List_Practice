'''16. Write a Python program to generate and print a list of first and last 5 elements 
      where the values are square of numbers between 1 and 30 (both included).
'''

list1=[]
list2=[]
for i in range(1,31):
      list1.append(i)
      list2.append(i**2)
print(list1)
print(list2)
print("For first five numbers:",list1[:5])
print("For first five numbers:",list2[:5])
print("For last five numbers:",list1[-5:])
print("For last five numbers:",list2[-5:])