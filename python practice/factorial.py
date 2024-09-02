# Python 3 program to find  
# factorial of given number
def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact *= n
            n -= 1
        return fact

# Driver Code
num = int(input("enter value "))
print("Factorial of",num,"is",
factorial(num))

# Python 3 program to find
# factorial of given number
 
# Function to find factorial of given number
def factorial(n):
      
    res = 1
     
    for i in range(2, n+1):
        res *= i
    return res
 # Driver Code
num = 5
print("Factorial of", num, "is",factorial(num))
###################
import numpy
n=5
x=numpy.prod([i for i in range(1,n+1)])
print(x)


#to find the factors of number

num=int(input("enter the number "))
for i in range(1,num+1):
    if num%i==0:
        print(i)
    