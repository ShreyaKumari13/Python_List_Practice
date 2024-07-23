'''
    56. Write a Python program to convert a string to a list.
'''
import ast
color ="['Red', 'Green', 'White']"
print(ast.literal_eval(color))


a=" [ I am navneet ] "
b=a.split()
print(b)