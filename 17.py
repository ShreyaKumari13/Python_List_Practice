'''
17. Write a Python program to generate and print a list except for the first 5 elements, 
    where the values are square of numbers between 1 and 30 (both included).
'''
list1=[]
list2=[]
for i in range(6,31):
      list1.append(i)
      list2.append(i**2)
print(list1)
print(list2)

def printValues():
	l = list()
	for i in range(1,31):
		l.append(i**2)
	print(l[5:])
printValues()

