str = input("enter the string :")
print("the original string is : ", str)
reverse_string = ""
count = len(str)
while count>0:
    reverse_string+=str[count-1]
    count=count-1
print("the reversed string :",reverse_string)

if str==reverse_string:
    print("palindrome")
else:
    print("not palindrome")