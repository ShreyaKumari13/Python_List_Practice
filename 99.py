'''
    99. Write a Python program to find the maximum and minimum values in a given heterogeneous list.
    Original list:
    ['Python', 3, 2, 4, 5, 'version']
    Maximum and Minimum values in the said list:
    (5, 2)
'''
list1 = ['Python', 3, 2, 4, 5, 'version']
list2 = []
for i in list1:
    if type(i)==int:
        list2.append(i)
a = min(list2)
b = max(list2)
print(b,a)


def max_min_val(list_val):
     max_val = max(i for i in list_val if isinstance(i, int)) 
     min_val = min(i for i in list_val if isinstance(i, int))
     return(max_val, min_val)
list_val = ['Python', 3, 2, 4, 5, 'version'] 
print("Maximum and Minimum values in the said list:")
print(max_min_val(list_val))
