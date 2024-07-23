'''
    55. Write a Python program to remove key values pairs from a list of dictionaries.
'''
original_list = [{'key1':'value1', 'key2':'value2'}, {'key1':'value3', 'key2':'value4'}]
new_list = [{k: v for k, v in d.items() if k != 'key1'} for d in original_list]

# for i in original_list:
#     for j in i.items():
#         if j!="key1"

for i in original_list:
    # for j in i:
    if i=="key1":
        i.pop("key1")
    
print(original_list)