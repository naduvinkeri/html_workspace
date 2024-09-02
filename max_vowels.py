
#vowels count
# str =input("enter the string ")
# words= str.split()
# max_vowel = ""
# max_vowel_count = 0
# for word in words:
#     vowel_count =0
#     for char in word:
#         if char in 'aeiouAEIOU':
#             vowel_count+=1
#         if vowel_count>max_vowel_count:
#             max_vowel_count=vowel_count
#             max_vowel = word
# print(max_vowel,max_vowel_count)


#python to give quardratic equation
import cmath

print("Coefficients of the quadratic equation ax^2 + bx + c = 0")
a=int (input("enter a value "))
b=int (input("enter b value "))
c=int (input("enter c value "))

if a == 0:
    print("The coefficient 'a' cannot be zero in a quadratic equation.")
else:
    discriminant = b**2 - 4*a*c
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    
    print(f"The roots of the quadratic equation are: {root1} and {root2}")


#linear program count the linear search of elements

#father is 3 times more than his son rohit after 8 year he could be 2 and half times of rohit each after 8

#to find sum of three 3 digits

#to read n number of string from user and check palindrome

#to display 3 digit palindrome

