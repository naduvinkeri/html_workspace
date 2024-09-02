size = int(input("Enter the size: "))
words = [input(f"Enter element {i+1}: ") for i in range(size)]
unique_words = []
for i in words:
    for word in i.split():
        if word not in unique_words:
            unique_words.append(word)
print("Word without duplicates:")
print(*unique_words, sep=" ")
