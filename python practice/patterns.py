#right angle 
# n = 5
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print('*', end=' ')
#     print()
# * 
# * *       
# * * *     
# * * * *   
# * * * * *

rows = 5  # Number of rows for the triangle
for i in range(rows):
    char = chr(ord('A') + (rows - 1- i))
    for j in range(i+1):
        print(char,end="")
    print()



#invert right angle
# n = 5
# for i in range(n, 0, -1):
#     for j in range(1, i + 1):
#         print('*', end=' ')
#     print()


#pyramid pattern
# n = 5
# for i in range(1, n + 1):
#     print(' ' * (n - i) + '* ' * i)


#diamond pattern
# n = 5
# # Upper part
# for i in range(1, n + 1):
#     print(' ' * (n - i) + '* ' * i)
# # Lower part
# for i in range(n - 1, 0, -1):
#     print(' ' * (n - i) + '* ' * i)


#hallow square
# n = 5
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n-1 or j == 0 or j == n-1:
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print()


#hallow triangle
# n = 5
# for i in range(n):
#     for j in range(i + 1):
#         if i == n-1 or j == 0 or j == i:
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print()


#pascal trianlge
# n = 5
# for i in range(n):
#     for j in range(n - i + 1):
#         print(end=" ")  # for spacing

#     C = 1
#     for j in range(1, i + 1):
#         print(C, end=" ")
#         C = C * (i - j) // j
#     print()
