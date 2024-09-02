my_array = [1, 2, 3, 2, 4, 1, 5, 2, 3]

# Create an empty dictionary to store frequencies
frequency_dict = {}

# Count the occurrences of each element
for elem in my_array:
    if elem in frequency_dict:
        frequency_dict[elem] += 1
    else:
        frequency_dict[elem] = 1


# Print the frequencies
for elem, freq in frequency_dict.items():
    print(f"Element {elem} occurs {freq} times")
