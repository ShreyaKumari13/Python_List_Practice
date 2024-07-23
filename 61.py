'''
    61. Write a Python program to create a list of empty dictionaries
'''

l=[]
for i in range(5):
    l.append({})
print(l)

n = 5
l = [{} for _ in range(n)]
print(l)

