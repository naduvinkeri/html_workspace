
#largest in the array
# arr=[]
# n=int(input("Enter the size of array "))
# arr=[0]*n
# for x in range(n):
#     arr[x]=int(input("enter the array "))


# largest = arr[0]
# smallest = arr[0]  

# for i in range(n):
#     if arr[i]>largest:
#         largest=arr[i]
#     if arr[i]<smallest:
#         smallest=arr[i]  
# print ("largest :",largest,"smallest :",smallest)


#second largest from 
number = [2, 1,10,24,15]
# # number.sort()
# # print(number[-2])

largest=0
second_largest=0
for num in number:                  #2 in number        1 in number
    if num>largest:                 #2>0                
        second_largest=largest      #sec_lar = 0
        largest=num                 #lar=2
    elif num>second_largest:                            #1>0
        second_largest=num                              #sec=1

print(largest,second_largest)



# number = [2, 1, 10, 24, 15]

# Initialize smallest and second smallest to a very high value
# smallest = float('inf')                                 #give any positive number
# second_smallest = float('inf')

# for num in number:
#     if num < smallest:                                 #to check largest num>smallest
#         second_smallest = smallest
#         smallest = num
#     elif num < second_smallest:
#         second_smallest = num

# print(smallest, second_smallest)






