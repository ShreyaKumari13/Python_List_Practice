'''
    97. Write a Python program to remove sublists from a given list of lists, which contains an element outside a given range.
    Original list:
    [[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]]
    After removing sublists from a given list of lists, which contains an element outside the given range:
    [[13, 14, 15, 17]]
'''
list1 = [[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]]
result = []
for i in list1:
    if min(i)>=11 and max(i)<=17:
        result.append(i)
        print(result)

def remove_list_range(input_list, left_range, rigth_range):
   result = [i for i in input_list if (min(i)>=left_range and max(i)<=rigth_range)]
   return result
list1 = [[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]]
left_range = 13
rigth_range = 17
print("After removing sublists from a given list of lists, which contains an element outside the given range:")
print(remove_list_range(list1, left_range, rigth_range))
