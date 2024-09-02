#to count the maximun number of letters

str1 = input("enter the string ")
words = str1.split()
longest_word =""
max_len=0

for word in words:
    if len(word) > max_len:
        max_len = len(word)
        longest_word=word
print("longest word ",longest_word)
print("length of longest word ",max_len)






