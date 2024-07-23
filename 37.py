'''
    37. Write a Python program to find common items from two lists.
'''
color1 = "Red", "Green", "Orange", "White","White"
color2 = "Black", "Green", "White", "Pink"
print(set(color1))
print(set(color2))
print(set(color1) & set(color2))
print(set(color1) | set(color2))

