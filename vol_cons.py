
#vowel and costuant
# str=input("enter the string ")
# vowel=['a','e','i','o','u']
# count_vowel= 0
# count_const=0
# for i in str.lower():
#     if i in vowel:
#         count_vowel+=1
#     else:
#         count_const+=1

# print("vowel ",count_vowel,"constuant ",count_const)


#count the special character letter digits
string=input("enter the string ")
letters=0
digits=0
special=0

for c in string:
    if c.isdigit():
        digits+=1
    elif c.isalpha():
        letters+=1
    else:
        special+=1
print(letters," ",digits," ",special)