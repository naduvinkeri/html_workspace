#linear search to find the index value

numbers=[1,4,3,4,4,6]
key_ele=2
result=-1
count=0
for i in range (0,len(numbers)):
    if numbers[i]==key_ele:
        result=i
       
        print(result)
        count+=1
if result==-1:
    print("not found") 
print(count) 

# arr=[]
# print("enter the 10 numbers ")
# for i in range(5):
#     arr.append(int(input("enter the number ")))
# print(arr)
# count=0
# for num in arr:
#     # print("negative ")
#     if num<0:
#         count+=1
#         print(num,end=" ")
# print()
# for num in arr:
#     # print("positive ")
#     if num>0:
#         count+=1
#         print(num,end=" ")
# print()
# print(count)


#prime number
# arr=[]                                   
# print("enter the 10 numbers ")
# for i in range(3):
#     arr.append(int(input("enter the number ")))  #apppending values of array
# print("prime numbers ") #1 2 6 
# count= 0
# for num in arr:               #1 in [ 1 2 6]
#     c=0
#     for j in range (1,num+1):  #j in [1, 1+1]
#         if num%j==0:           
#             c+=1
#     if c==2:
#         print(num,end=" ")
#         count+=1
# print("the number of prime ",count,end="")





    
    

   


