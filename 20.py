'''
    20. Write a Python program access the index of a list.

'''


list1=[1,2,3,4,5]
for index,i in enumerate(list1):
    print(f"at index {index} the element is {i}")














# a='''At first we attempted to explain, but in most instances, we failed 1 2 3 4 5 to clarify our reasons.'''
# sum1,sum2,sum3,sum4,sum5,sum6=0,0,0,0,0,0
# b=a.split(" ")
# print("No.of words",len(b))
# for i in a:
#     if i.isalpha():
#         sum1=sum1+1
#         if i.lower() in["a","e","i","o","u"]:
#             sum5=sum5+1
#         if i.lower() not in['a','e','i','o','u']:
#             sum6=sum6+1
#     elif i.isdigit():
#         sum2=sum2+1
#     elif i.isspace():
#         sum3=sum3+1
#     else:
#         sum4=sum4+1
# print("No.of letters",sum1)
# print("No.of digits",sum2)
# print("No.of spaces",sum3)    
# print("No.of special character",sum4)
# print("No.of vowels",sum5)
# print("No.of consonants",sum6)







# a = "Navneet is a 143"
# b=a.split(" ")
# c = []
# print(b)
# for i in b:
#     try :
#         c.append(i)
#         c.append(int(i))
#         c.append(i)
#     except:
#         pass
# print(c)