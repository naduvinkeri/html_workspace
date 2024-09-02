#calculator without using + - * /

m= int(input("enter num 1 "))
n= int(input("enter num 2 "))

choice = int(input("enter choice 1: add 2: mul 3: div "))

result=0

if choice==1:
    result=m-(-n)
elif choice==2:
    for i in range(1, n+1): 
        result +=m 
elif choice==3:
    while m>=n: #check again value of m
        m-=n 
        result +=1 
        

print(result)


