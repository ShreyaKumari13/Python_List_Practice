'''
    70. Write a Python program to find the items starts with specific character from a given list.
    Expected Output:
    Original list:
    ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
    Items start with a from the said list:
    ['abcd', 'abc', 'acjd']
    Items start with d from the said list:
    ['dagfa']
    Items start with w from the said list:
    []
'''
list1 = ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
list2=[]
list3=[]
list4=[]
list5=[]
list6=[]
for i in list1:
    if i[0]=="a":
        list2.append(i)
    elif i[0]=="b":
        list3.append(i)
    elif i[0]=="c":
        list4.append(i)
    elif i[0]=="d":
        list5.append(i)
    elif i[0]=="s":
        list6.append(i)
    else:
        break
print("Items start with a from the said list:",list2)
print("Items start with b from the said list:",list3)
print("Items start with c from the said list:",list4)
print("Items start with d from the said list:",list5)
print("Items start with s from the said list:",list6)


def test(lst, char):
    for i in lst:
        result=[]
        if i.startswith(char):
            result.append(i)
            print(result)
text = ["abcd", "abc", "bcd", "bkie", "cder", "cdsw", "sdfsd", "dagfa", "acjd"]

char = "a"
print("\nItems start with",char,"from the said list:")
test(text, char)

char = "d"
print("\nItems start with",char,"from the said list:")
test(text, char)

char = "w"
print("\nItems start with",char,"from the said list:")
test(text, char)
