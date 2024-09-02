# def is_armstrong_number(number):
# 	return sum(int(digit)**len(str(number)) for digit in str(number)) == number


# # Example usage:
# num = int(input("enter the number "))
# if is_armstrong_number(num):
# 	print(f"{num} is an Armstrong number")
# else:
# 	print(f"{num} is not an Armstrong number")

#armstrong number
user_number = int(input("Enter a number: "))
num_str = str(user_number)
num_digits = len(num_str)
armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)

if armstrong_sum == user_number:
    print(f"{user_number} is an Armstrong number!")
else:
    print(f"{user_number} is not an Armstrong number.")
