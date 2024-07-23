'''
    92. Write a Python program to check if a nested list is a subset of another nested list.
    Original list:
    [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
    [[1, 3], [13, 15, 17]]
    If the one of the said list is a subset of another.:
    True
    Original list:
    [[[1, 2], [2, 3]], [[3, 4], [5, 6]]]
    [[[3, 4], [5, 6]]]
    If the one of the said list is a subset of another.:
    True
    Original list:
    [[[1, 2], [2, 3]], [[3, 4], [5, 7]]]
    [[[3, 4], [5, 6]]]
    If the one of the said list is a subset of another.:
    False
'''
def truefalse(list1,list2):
    for i in list1:
        for j in list2:
            if i==j:
                return True
            else:
                return False
list1 = [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
list2 = [[1, 3], [13, 15, 17]]
a = truefalse(list1,list2)
print(a)

def checkSubset(list1,list2): 
    return all(map(list1.__contains__,list2)) 
list1 = [[1, 3], [5, 7], [9, 11], [13, 15, 17]] 
list2 = [[1, 3],[13,15,17]]   
print("\nIf the one of the said list is a subset of another.:")
print(checkSubset(list1, list2)) 

