'''
    84. Write a Python program to round the numbers of a given list, print the minimum and maximum 
    numbers and multiply the numbers by 5. Print the unique numbers in ascending order separated by space.
    Original list: [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
    Minimum value: 4
    Maximum value: 22
    Result:
    20 25 45 55 60 70 80 90 110
'''
list1 = [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
a = list(map(round,list1))
print("min = ",min(a))
print("max = ",max(a))
a.sort()
for i in a:
    print(i*5,end=" ")


nums = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
numbers=list(map(round,nums))
print("\nMinimum value: ",min(numbers))
print("Maximum value: ",max(numbers))
numbers=list(set(numbers))
numbers=(sorted(map(lambda n:n*5,numbers)))
for numb in numbers:
    print(numb,end=' ')
