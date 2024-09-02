
# #1 to find the sum of digits of given number
# number = int(input("enter the number "))
# sum_of_digits = 0

# while number > 0:
#     sum_of_digits += number % 10
#     number = number // 10

# print("sum ",sum_of_digits)



#M2 using for loop and converting int into str
# number = 12345
# sum_of_digits = 0

# for digit in str(number):
#     sum_of_digits += int(digit)

# print(f"The sum of the digits of {number} is {sum_of_digits}")



# 2 print the pattern 
# 34
# 2
# 234
# 1234
# for i in range(3,5):
#     print(i,end=" ") #3 4
# print() #next line
# print(2)
# for i in range(2,5):
#     print (i,end=" ")
# print()
# for i in range(1,5):
#     print(i,end=" ")



# 3 store 20 number in single dimensional array and display array
# user_array = []
# primes=[]
# array_length = int(input("Enter the length of the array: "))
# for i in range(array_length):
#     user_input = int(input(f"Enter element {i+1}: "))
#     user_array.append(user_input)
# print("User input array:", user_array)

#to find the prime number in given array
# for num in user_array:
#     if num > 1:  
#         is_prime = True
#         for i in range(2, int(num**0.5) + 1):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             primes.append(num)
# print(primes)



#4 to find the largest and smallest number
# user_array = []
# array_length = int(input("Enter the length of the array: "))
# i = 0
# while i < array_length:
#     user_input = int(input("Enter element {}: ".format(i + 1)))
#     user_array.append(user_input)
#     i += 1
# largest = user_array[0]
# smallest = user_array[0]

# Iterate through the array to find largest and smallest
# for num in user_array:
#     if num > largest:
#         largest = num
#     elif num < smallest:
#         smallest = num

# print("User input array:", user_array)
# print(f"Largest number: {largest}")
# print(f"Smallest number: {smallest}")





# #5 to count the even and odd number
# user_array = []

# array_length = int(input("Enter the length of the array: "))

# #to take the elements of array
# i = 0
# while i < array_length:
#     user_input = int(input("Enter element {}: ".format(i + 1)))
#     user_array.append(user_input)
#     i += 1

# # Initialize counters for even and odd numbers
# even_count = 0
# odd_count = 0

# Iterate through the array to count even and odd numbers
# for num in user_array:
#     if num % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1

# print("User input array:", user_array)
# print(f"Even numbers count: {even_count}")
# print(f"Odd numbers count: {odd_count}")


#3.	Calculate the salary of a camera salesman. His basic salary is Rs.25000/-,
# for every camera he will sell he will get Rs.200/- and the commission on
# the month’s sale is 12 %. The input will be number of cameras sold and the
# price of the camera.

# n_camera = int (input("enter the no of cameras sold for this month "))
# camera_price = float(input("enter the price "))
# total_sales = camera_price * n_camera 
# basic_salary =25000 
# salary = basic_salary + n_camera *200 +total_sales * 0.12 
# print(f'salary = rs{salary}')

#to find the leap year with out using arthmatic operators % / 
# Check if the year is divisible by 4
# divisible_by_4 = year_str[-2:] in ["00", "04", "08", "12", "16", "20", "24", "28", "32", "36", "40", "44", "48", "52", "56", "60", "64", "68", "72", "76", "80", "84", "88", "92", "96"]

# Check if the year is divisible by 100
# divisible_by_100 = year_str[-2:] == "00" and year_str[-4:-2] in ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92", "93", "94", "95", "96", "97", "98", "99"]

# Check if the year is divisible by 400
# divisible_by_400 = year_str[-2:] == "00" and year_str[-4:] in ["0000", "0400", "0800", "1200", "1600", "2000", "2400", "2800", "3200", "3600", "4000", "4400", "4800", "5200", "5600", "6000", "6400", "6800", "7200", "7600", "8000", "8400", "8800", "9200", "9600"]



# divisible_by_4 = year_str[-2:] in range(00,100,4)

# divisible_by_100 = year_str[-2:] == "00" and year_str[-4:-2] in range(00,100)
# divisible_by_400 = year_str[-2:] == "00" and year_str[-4:] in range(0000,10000,4)
# # A year is a leap year if it is divisible by 4, but not by 100, unless it is also divisible by 400
# is_leap = divisible_by_4 and not divisible_by_100 or divisible_by_400

# print(f"The year {year} is a leap year: {is_leap}")



#to find the sum of second and last digits
# number = int(input("enter the number "))
# number_str = str(number)

# # Get the second digit
# second_digit = int(number_str[1])

# # Get the last digit
# last_digit = int(number_str[-1])

# # Calculate the sum of the second and last digits
# sum_of_digits = second_digit + last_digit
# print(f"The sum of the second and last digits of {number} is {sum_of_digits}")




#to swap to string without using third variables
a=(input("enter the  string "))
b=(input("enter the string "))
a,b=b,a
print(a,b)


#to eliminate duplicate words







