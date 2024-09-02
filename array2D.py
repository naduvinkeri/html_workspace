# 2D array use for graphs data analysis tables machine learning vizualization 
# rows = int(input("enter the rows "))
# column = int(input("enter the column "))

# arr = [[0 for i in range(column)] for j in range(rows)]
# for i in range(rows):
#     arr[[i][j]] = len(rows)

# for i in range(rows):
#     for j in range(column):


# rows = int(input("Enter the number of rows: "))
# columns = int(input("Enter the number of columns: "))
# arr = [[0 for i in range(columns)] for j in range(rows)]

# for i in range(rows):
#     for j in range(columns):
#         arr[i][j] = i * columns + j
# for row in arr:
#     print(row)

# rows = int(input("Enter the number of rows: "))
# columns = int(input("Enter the number of columns: "))

# arr = [[0 for i in range(columns)] for j in range(rows)]

# for i in range(rows):
#     for j in range(columns):
#         arr[i][j] = int(input(f"Enter value for cell ({i}, {j}): "))

# for row in arr:
#     print(row)



# Get the dimensions of the 2D array from the user

# rows = int(input("Enter the number of rows: "))
# cols = int(input("Enter the number of columns: "))
# array_2d = []
# for i in range(rows):
#     row = []
#     for j in range(cols):
#         value = input(f"Enter value for element at position ({i}, {j}): ")
#         row.append(value)
#     array_2d.append(row)
# print("\nYour 2D array:")
# for row in array_2d:
#     print(" ".join(row))

    


#to read n number of students and display pass and fail
num1= int(input("enter the sub1 marks "))
num2= int(input("enter the sub2 marks "))
avg=(num1+num2)/2
if num1>=50 and num2>=50 and avg>=50:
    print("pass")
else:
    print("fail")
