
#to find the sum of first and last number
num= int(input("enter the number ")) #123
count=0
while num!=0:
    if count==0:
        last = num%10 #remainder  3
        
        count+=1
    first =num%10 #123%10=3
    num=num//10  #quoient
print(first+last) 
