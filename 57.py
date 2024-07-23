'''
    57. Write a Python program to check whether all items of a list is equal to a given string.
'''
color1 = ["green", "orange", "black", "white"]
color2=  ["green","green","green","green",]
for i in color1:
    if i=="green":
        print(True)
    pass
for i in color2:
    if i=="green":
        print(True)
    pass

# color1 = ["green", "orange", "black", "white"]
# color2 = ["green", "green", "green", "green"]
# print(all(c == 'blue' for c in color1))
# print(all(c == 'green' for c in color2))
