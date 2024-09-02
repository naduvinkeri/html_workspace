def fact(num):
    i=1
    while i!=num:
        num=num//i
        i+=1
    return num

num=120
result=fact(num)
print(result)
