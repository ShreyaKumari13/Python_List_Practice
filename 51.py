'''51. Write a Python program to split a list every Nth element. Go to the editor
Sample list: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
Expected Output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
Click me to see the sample solution

'''
c = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
n=int(input("Enter the nth element: "))
for i in c:
    a=c[::n]
    b=c[1::n]
    d=c[2::n]
list4=[]
list4.append(a)
list4.append(b)
list4.append(d)
print(list4)

def list_slice(S, step):
    return [S[i::step] for i in range(step)]
C = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
print(list_slice(C,3))



