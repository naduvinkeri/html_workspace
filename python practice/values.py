# a=int(input("a "))
# b=int(input("a "))
# if a<=0:
#     b=b+1
# else:
#     a=a+1
# print(6%5) #remainder
 
# double the number without using arithmetic operator
# num=int(input("Enter a number: "))

# print(num<<1)

num = int(input('Enter a number :'))

arr = []

for i in range(2,num):

    flag = 0

    for j in range(2,i):

        if i % j == 0:

            flag = 1

    if flag == 0:

        arr.append(i)

flag = 0

for i in range(len(arr)):

    for j in range(i+1,len(arr)):

        if(arr[i] + arr[j] == num):

            flag = 1

            print(str(num) + " can be expressed as the sum of " + str(arr[i]) + " and " + str(arr[j]))

            break

if(flag == 0):

    print('No Prime numbers can give sum of ' + str(num))

