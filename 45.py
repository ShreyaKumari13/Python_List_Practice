'''
    45. Write a Python program to convert a pair of values into a sorted unique array.

'''
list1=[(1,2),(1,2),(3,4),(3,4)]
print(set(list1))









print('  __  __          _____ _____ _____    ')
print(' |  \/  |   /\   / ____|_   _/ ____| ')
print(' | \  / |  /  \ | |  __  | || |      ')
print(' | |\/| | / /\ \| | |_ | | || |       ')
print(' | |  | |/ ____ \ |__| |_| || |____  ')
print(' |_|  |_/_/    \_\_____|_____\_____|  ')
print()

a = int(input("Enter The Date : "))
b = input("Enter The Month : ")
if b=='1':
    if a>=20 and a<=31:
        print("Aquarius")
    else:
        print("Capricorn")
if b=='2':
    if a>=19 and a<=29:
        print("Pisces")
    else:
        print("Aquarius")
if b=='3':
    if a>=21 and a<=31:
        print("Aries")
    else:
        print("Pisces")
if b=='4':
    if a>=20 and a<=30:
        print("Taurus")
    else:
        print("Aries")
if b=='5':
    if a>=21 and a<=31:
        print("Gemini")
    else:
        print("Taurus")
if b=='6':
    if a>=21 and a<=30:
        print("Cancer")
    else:
        print("Gemini")
if b=='7':
    if a>=23 and a<=31:
        print("Leo")
    else:
        print("Cancer")
if b=='8':
    if a>=23 and a<=31:
        print("Virgo")
    else:
        print("Leo")
if b=='9':
    if a>=23 and a<=30:
        print("Libra")
    else:
        print("Virgo")
if b=='10':
    if a>=23 and a<=31:
        print("Scorpio")
    else:
        print("Libra")
if b=='11':
    if a>=22 and a<=30:
        print("Sagittarius")
    else:
        print("Scorpio")
if b=='12':
    if a>=22 and a<=31:
        print("Capricorn")
    else:
        print("Sagittarius")

