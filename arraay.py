
# rows = int(input("Enter the number of rows: "))
# columns = int(input("Enter the number of columns: "))

# # Initialize an empty matrix
# matrix = []
# diagonal_sum =0
# anti_diagonal_sum=0


# # Populate the matrix
# for i in range(rows):
#     row = []
#     for j in range(columns):
#         value = int(input(f"Enter value for matrix[{i}][{j}]: "))
#         row.append(value)
#         if i == j:  # Check if the element is on the diagonal
#             diagonal_sum += value
#         if i + j == columns - 1:  # Anti-diagonal (top right to bottom left)
#             anti_diagonal_sum += value
#     matrix.append(row)


# # Print the matrix
# print("The matrix is:")
# for row in matrix:
#     for value in row:
#         print(value, end=" ")
#     print()
# #index value
# print("The matrix with indices is:")
# for i in range(rows):
#     for j in range(columns):
#         print(f"matrix[{i}][{j}] = {matrix[i][j]}", end="    ")
#     print()

# print("The sum of the diagonal elements is:", diagonal_sum)
# print("The sum of the diagonal elements is:", anti_diagonal_sum)


# Get the size of the identity matrix (rows and columns should be the same)
size = int(input("Enter the size of the identity matrix: "))
matrix = []

# Populate the matrix with 1s on the main diagonal and 0s elsewhere
for i in range(size):
    row = []
    for j in range(size):
        if i == j:  # Main diagonal (where row index equals column index)
            row.append(1)
        else:
            row.append(0)
    matrix.append(row)

# Print the identity matrix
print("The identity matrix is:")
for row in matrix:
    for value in row:
        print(value, end=" ")
    print()

