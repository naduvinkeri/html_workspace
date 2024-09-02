even_sum=0
odd_sum=0

while True:
    number=int(input("enter the number ")) # 2 3 4
    if number %2==0:    #4%2==0 0==0
        even_sum+=number #0+2=2+4=6
    else:
        odd_sum+=number # 0+3=3

    choice=input("do u want to continue (y/n) ").lower() # Y y n

    if choice!='y': # y
        break
print("sum of even number",even_sum)

print("sum of odd number",odd_sum)