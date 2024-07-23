'''
    85. Write a Python program to create a multidimensional list (lists of lists) with zeros.
    Multidimensional list: [[0, 0], [0, 0], [0, 0]]
'''
nums = []
for i in range(3):
    nums.append([])
    for j in range(2):
        nums[i].append(0)
print("Multidimensional list:")
print(nums)
