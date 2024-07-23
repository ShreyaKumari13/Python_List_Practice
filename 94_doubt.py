'''
    94. Write a Python program to count number of unique sublists within a given list.
    Original list:
    [[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]
    Number of unique lists of the said list:
    {(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
    Original list:
    [['green', 'orange'], ['black'], ['green', 'orange'], ['white']]
    Number of unique lists of the said list:
    {('green', 'orange'): 2, ('black',): 1, ('white',): 1}
'''
list1 = [[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]
list1.sort()
count=0
for i in list1:
    if list1[i]==list1[i+1]:
        count+=1
    print(count)

