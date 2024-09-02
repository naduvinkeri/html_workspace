#find lcm of any two number

m= int(input("enter num 1 "))
n= int(input("enter num 2 "))

greater=1

while(True):
    if greater%m==0 and greater%n==0: # do till both m n get remaindar == 0
        lcm=greater
        break
    greater+=1

print(lcm) 

