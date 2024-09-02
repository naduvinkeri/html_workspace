#3 digit palindrome with in the range 

min=int(input("enter the min value ")) #100
max=int(input("enter the max value ")) #200

for num in range(min,max+1):
    temp=num
    rev=0
    while (temp>0):
        remindar= temp %10
        rev=(rev*10)+remindar
        temp = temp//10
    if(num==rev):
        print(num)


