'''
    5. Write a Python program to count the number of strings where 
    the string length is 2 or more and the first and last character 
        are same from a given list of strings. 
    Sample List : ['abc', 'xyz', 'aba', '1221']
    Expected Result : 2
'''
a=['abc', 'xyz', 'aba', '1221']
b=len(a)
count=0
if (b>=2):
    for i in a:
        if i[0]==i[-1]:
            print(i)
            count+=1
print("Total number of same string:",count)
