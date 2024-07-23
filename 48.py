'''
    48. Write a Python program to print a nested lists (each list on a new line) using the print() function.
'''
colors = [['Red'], ['Green'], ['Black']]
for i in colors:
    print(i)

colors = [['Red'], ['Green'], ['Black']]
print('\n'.join([str(lst) for lst in colors]))

