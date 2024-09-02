# num=int(input("enter the number"))
# temp=num
# rev=0
# while num!=0:
#     digit=num%10
#     rev=rev*10+digit
#     num//=10
# print(rev)
# if(temp==rev):
#     print("palindrome")

# if (num==rev):
#     print(rev)
# else:
#     print(rev)

str=input("enter the string ")
reverse_string = ""
count =len(str)
while count>0:
    reverse_string += str[count - 1]
    count=count-1

if(str==reverse_string):
    print("palindrome")
else:
    print("not palindrome")
