



# a=153%10 #count  %2 == remainder
# print(a)
# 
# a=12345//10 #1234
# print(a)

num = int(input("Enter the number: "))
# a = int(input("Enter the number of digits: "))
sum = 0
# temp = num

# while num != 0:
#     digit = num % 10
#     sum += digit ** a
#     num //= 10

# if temp == sum:
#     print("Armstrong")
# else:
#     print("Not Armstrong")


# sum of numbers
while num!=0:
    n1=num%10 #153%10 = 3
    sum+=n1 
    num//=10 #153//10 = 15
print(sum) #153=> 1+5+3=9


