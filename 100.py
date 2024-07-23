'''
    100. Write a Python program to extract common index elements from more than one given list.
    Original lists:
    [1, 1, 3, 4, 5, 6, 7]
    [0, 1, 2, 3, 4, 5, 7]
    [0, 1, 2, 3, 4, 5, 7]
    Common index elements of the said lists:
    [1, 7]
'''
list1 = [1, 1, 3, 4, 5, 6, 7]
list2 = [0, 1, 2, 3, 4, 5, 7]
list3 = [0, 1, 2, 3, 4, 5, 7]
list4 = []
for i,j,k in zip(list1,list2,list3):
    if i==j==k:
        list4.append(i)
print(list4)

def extract_index_ele(l1, l2, l3):
    result = []
    for m, n, o in zip(l1, l2, l3):
        if (m == n == o):
            result.append(m)
    return result
nums1 = [1, 1, 3, 4, 5, 6, 7]
nums2 = [0, 1, 2, 3, 4, 5, 7]
nums3 = [0, 1, 2, 3, 4, 5, 7]
print("Common index elements of the said lists:") 
print(extract_index_ele(nums1, nums2, nums3))

