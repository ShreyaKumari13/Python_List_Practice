''' 
    63. Write a Python program to insert a given string at the beginning of all items in a list.
    Sample list : [1,2,3,4], string : emp
    Expected output : ['emp1', 'emp2', 'emp3', 'emp4']
'''
# num = [1,2,3,4]
# print(['emp{0}'.format(i) for i in  num])

num=[1,2,3,4]
num2=[]
for i in num:
    num2.append("emp{0}".format(i))
print(num2)

num=[1,2,3,4]
for i in range(len(num)):
    num[i] = f"emp{i+1}"
print(num)

num=[1,2,3,4]
for i in range(len(num)):
    num[i] = 'emp'+ str(num[i])
print(num)