'''
    95. Write a Python program to sort each sublist of strings in a given list of lists.
    Original list:
    [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
    Sort the list of lists by length and value:
    [[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]
'''
list1 = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
result = list(map(sorted,list1))
print(result)


def sort_sublists(input_list):
    result = list(map(sorted, input_list)) 
    return result
list1 = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
a = sort_sublists(list1)
print(a)

