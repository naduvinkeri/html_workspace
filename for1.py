str=input("enter the string ")
alpha1=digit=special1=''
for c in str:
    if c.isalpha():
        alpha1+=c
    elif c.isdigit():
        digit+=c
    else:
       special1+=c
print("alpha",alpha1)
print("digit",digit)
print("special",special1)

#to print the value in string

str=input("enter the string ")
alpha1=digit=special1=0
for c in str:
    if c.isalpha():
        alpha1+=1
    elif c.isdigit():
        digit+=1
    else:
       special1+=1
print("alpha",alpha1)
print("digit",digit)
print("special",special1)
