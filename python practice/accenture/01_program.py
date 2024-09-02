# Integers divisible by 6 are 6, 12, 18, 24, and 30. Their sum is 90.
# Integers that are not divisible by 6 are 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 25, 26, 27, 28, and 29. Their sum is 375.
# The difference between them is 285 (375 – 90).
def difference_of_sum(m, n):
    # Initialize sums for divisible and non-divisible integers
    divisible_sum = 0
    non_divisible_sum = 0

    # Iterate through all integers from 1 to n (inclusive)
    for num in range(1, n + 1):
        if num % m == 0:
            # If divisible by m, add to divisible_sum
            divisible_sum += num
        else:
            # Otherwise, add to non_divisible_sum
            non_divisible_sum += num

    # Calculate the difference
    difference = non_divisible_sum - divisible_sum
    return difference

# Example usage:
m = 6
n = 30
result = difference_of_sum(m, n)
print(f"The difference between sums: {result}")
