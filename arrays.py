#arrays to read and display
# dept=[input(f"enter the dept {i+1}: ") for i in range(3)] #[1 2 3]
# for i in dept:
#     print(i) 
# #cs ece is
# # 123
# # $%#
# print(dept) #['cs ece is', '123', '$%#']
# print(*dept) # cs ece is 123 $%#  to remove [ ] use *

#initalization of array
a= [10,20,30,3]
# for i in a:
#     print(i)
# for i in range(1,3):
#     print(a[i])
# for i in range(4):
# sum=a[0]+a[2]
# print(sum)

# count=0
# for i in a:
#     count+=1
# print(count)

# sum1=0
# for i in a:
#     sum1+=i
# print(sum1)

# print("avg ",sum1//count)

#even and odd
# for i in a:
#     if i%2==0:
#         print(i)
#     else:
#         print(i)



import array as arr
numbers=arr.array("i", [1,2,3]) #float we get type error
print(numbers)
