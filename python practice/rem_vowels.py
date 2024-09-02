input_string = input("enter the string ")
vowels = "aeiouAEIOU"
result_string = ""

for char in input_string:
    if char not in vowels:
        result_string += char

print(result_string)