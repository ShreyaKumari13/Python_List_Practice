'''
    10. Write a Python program to find the list of words that are longer than n from a given list of words. 

'''
sentence = input("Enter sentence: ")
longest = max(sentence.split(), key=len)
print("Longest word is: ", longest)
print("And its length is: ", len(longest))


list1=["SHREYA","NAVNEET","SRUTI"]
longest = max(list1,key=len)
print("Longest word is: ", longest)
print("And its length is: ", len(longest))

def long_words(n, str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len	
print(long_words(3, "The quick brown fox jumps over the lazy dog"))

