'''
    83. Write a Python program to round every number of a given list of numbers and print the
    total sum multiplied by the length of the list.
    Original list: [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
    Result:
    243
'''
list1 = [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
list2 = []
a=len(list1)
for i in list1:
    list2.append(round(i,0))
print(sum(list2)*a)

nums = [22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50]
length=len(nums)
print(sum(list(map(round,nums))* length)) 
