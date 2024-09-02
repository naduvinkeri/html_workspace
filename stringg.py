# str = " string"
# print(str)

# size = int (input())
# words_array = (input(f"{i+1}") for i in range(size)) 
# prev_word = [None] * size
# current_index= 0
# for word in words_array:
#     is_duplicate = False

#     for unique in prev_word:
#         if unique==word:
#             is_duplicate=True
#             break
#         if not is_duplicate:
#             prev_word[current_index] = word
#             current_index+=1
# for i in range (current_index):
#     print(prev_word[i], end=" ")

#to remove duplicate
# size = int(input("Enter the size: "))
# words_array = [input(f"Enter element {i+1}: ") for i in range(size)]

# # Initialize an empty list to store unique words
# unique_words = []

# # Traverse the words_array and filter out duplicates
# for word in words_array:
#     if word not in unique_words:
#         unique_words.append(word)

# # Display the cleaned word array
# print("Word array without duplicates:")
# print(*unique_words, sep=" ")


size = int(input("Enter the size: "))
words_array = [input(f"Enter element {i+1}: ") for i in range(size)]
unique_words = []
for phrase in words_array:
    for word in phrase.split():
        if word not in unique_words:
            unique_words.append(word)
print("Word array without duplicates:")
print(*unique_words, sep=" ")




