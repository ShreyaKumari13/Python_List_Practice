'''
    6. Write a Python program to get a list, sorted in increasing order by the last 
        element in each tuple from a given list of non-empty tuples. Go to the editor
    Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
    
'''
def Sort_Tuple(tup): 
    lst = len(tup) 
    for i in range(0, lst):  
        for j in range(0, lst-i-1): 
            if (tup[j][1] > tup[j + 1][1]): 
                temp = tup[j] 
                tup[j]= tup[j + 1] 
                tup[j + 1]= temp 
    return tup 
tup =[(1, 2),(2, 1)]   
print(Sort_Tuple(tup)) 

# def last(n): 
#     return n[-1]
# def sort_list_last(tuples):
#   return sorted(tuples, key=last)

# print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

