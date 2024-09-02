n =int(input(" enter the number "))
l = []
while n!=0:
    r = n%2
    l=[r]+l
    n//=2

print(l)

#remove bracket
for i in l:
    print(i,end=" ")

