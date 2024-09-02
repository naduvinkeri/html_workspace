# #gcd
num1 = int(input("enter num1 "))
num2 = int(input("enter num2 "))
gcd=1
for i in range(1,min(num1,num2)):
    if num1%i==0 and num2%i==0:
        gcd=i
print(gcd)

# while num2>0:
#     temp=num2
#     num2=num1%num2
#     num1=temp
# gcd=num1
# print("gcd ",gcd)



#using while
# while num1 != num2:
#     if num1 > num2:
#         num1 -= num2
#     else:
#         num2 -= num1
# print(num1)  #this fails if num1or num2 =0


#when num are 0
# def findGCD(num1, num2):
#     if num1 == 0 or num2 == 0:
#         return num1 + num2
    
#     # base case
#     if num1 == num2:
#         return num1
    
#     # num1>num2
#     if num1 > num2:
#         return findGCD(num1 - num2, num2)
#     else:
#         return findGCD(num1, num2 - num1)

# print(findGCD(num1,num2))



#find the value of factorial 120=5!
# n=int(input("enter the number "))
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)

#to find number
# given_factorial = int(input("enter the factorial value "))
# if given_factorial == 1 :
#     number = 1  # 0! and 1! are both 1
# else:
#     n = 1
#     product = 1
#     while product < given_factorial:
#         n += 1
#         product *= n

#     if product == given_factorial:
#         number = n
#     else:
#         number = None  # The given value is not a factorial of any integer

# if number is not None:
#     print(f"The number whose factorial is {given_factorial} is {number}")
# else:
#     print(f"No number found whose factorial is {given_factorial}")



#pattern

#prime number with in the range
# start = 10
# end = 50

# for num in range(start, end + 1):
#     if num > 1:  # 1 is not a prime number
#         is_prime = True
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             print(num, end=' ')



#leap yr without using modulus
# year = int(input("enter the year "))
# divisible_by_4 = year - (year // 4) * 4 == 0
# divisible_by_100 = year - (year // 100) * 100 == 0
# divisible_by_400 = year - (year // 400) * 400 == 0
# if divisible_by_4:
#     if divisible_by_100:
#         if divisible_by_400:
#             leap_year = True
#         else:
#             leap_year = False
#     else:
#         leap_year = True
# else:
#     leap_year = False


# if leap_year:
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")


#armstrong number 3 digit with in the range



#prime using array sum and count
# Given array
# array = [1,2,3]
# primes = []
# count=0
# sum=0
# for num in array:
#     if num > 1:  
#         is_prime = True
#         for i in range(2, int(num**0.5) + 1):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             primes.append(num)
#             sum+=num
#             count+=1



# print("Prime numbers in the array:", *primes)
# print("count ",count)
# print("sum ",sum)
# print("avg ",sum/count)


# even number in range 100 to 200
# num=100
# while  num<=200:
#     if num%2==0:
#         print(num)
#     num+=1

#palindrome

