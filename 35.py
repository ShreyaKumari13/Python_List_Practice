'''
    35. Write a Python program to create a list by concatenating a given list which range goes from 1 to n.
    Sample list : ['p', 'q']
    n =5
    Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
'''
list1=["p","q"]
list2=["1","2","3","4","5"]
list3=[]
for i in list2:
    for j in list1:
        a=i+j
        list3.append(a)
print(list3)


my_list = ['p', 'q']
n = 5
new_list=[]
for x in my_list:
    for y in range(1,n+1):
        new_list.append(f"{x}{y}")
print(new_list)


my_list = ['p', 'q']
n = 5
new_list=[]
for x in my_list:
    for y in range(1,n+1):
        new_list.append("{}{}".format(x,y))
print(new_list)