#in python there are only two loop
# For loop and while loop there is no DO while loop in python
#for loop is used for sequence data types like set tuple list string deictonary and range
# for loop is not used in int data type

# syntax for for Loop 

# for i in sequence:
#     statements
#     statements
#     statements

# x = [10,20,30,40,50]
# for i in x:
#     print (i) 
# #10
# 20
# 30
# 40
# 50

# x = "manoj"
# for i in x:
#     print(i)


# for i in range(1,21): #1-20
#     print(i)

# multilple of any number in range
# to get range use range function along with for Loop 
# ex== for i in range(1,201) #1-200
# then use % == 0 to check if it is divisible by number

# Ex 

# for i in range(1,201):
#     if i%3==0 and i%2==0:
#         print(i)

# to skip any number take ! not equal to zero in if condition

# EX 

# for i in range(1,7):
#     if i%3!=0:
#         print(i) #this will skip multiple of 3

# other method to skip any number

# for i in range(1,10):
#     if i!=3 and i!=4 and i!=7:
#         print(i) 
# 1
# 2
# 5
# 6
# 8
# 9

# fizz buzz

# for i in range(1,16):
#     if i%3==0 and i%5==0:
#         print(i,"FizzBuzz")
#     elif i%3==0:
#         print(i,"Fizz")
#     elif i%5==0:
#         print(i,"Buzz")

# to print the multiplication table
# n=multiplication

n=int(input("Enter the n value"))
for i in range(1,11):
    print(i*n)