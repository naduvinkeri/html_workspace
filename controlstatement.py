#if is used to check for true
a= int (input("enter the value "))
b= int (input("enter the value "))
c= int (input("enter the value "))
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
elif c>a and c>b:
    print(c)
else:
    print("equal")