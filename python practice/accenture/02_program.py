def separate_even_odd(arr):
    even_elements = []
    odd_elements = []

    for num in arr:
        if num % 2 == 0:
            even_elements.append(num)
        else:
            odd_elements.append(num)

    return even_elements, odd_elements

def find_second_largest(nums):
    nums.sort(reverse=True)
    return nums[1] if len(nums) >= 2 else None

# Input from the user
user_input = input("Enter space-separated integers for the array: ")
arr = list(map(int, user_input.split()))

# Separate even and odd elements
even_nums, odd_nums = separate_even_odd(arr)

# Find the second largest even and odd elements
second_largest_even = find_second_largest(even_nums)
second_largest_odd = find_second_largest(odd_nums)

if second_largest_even is not None and second_largest_odd is not None:
    difference = second_largest_even - second_largest_odd
    print(f"Difference between second largest even and second largest odd: {difference}")
else:
    print("Insufficient elements to calculate the difference.")

