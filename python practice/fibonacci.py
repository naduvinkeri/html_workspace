# num = int(input("Enter the Number:"))
# n1, n2 = 0, 1
# print("Fibonacci Series:", n1, n2, end=" ")
# for i in range(2, num):
#     n3 = n1 + n2
#     n1 = n2
#     n2 = n3
#     print(n3, end=" ")

# print()

# def fibonacci(n):
#     fib_series = [0, 1]  # Initialize the series with the first two numbers

#     while len(fib_series) < n:
#         next_num = fib_series[-1] + fib_series[-2]
#         fib_series.append(next_num)

#     return fib_series

# # Example usage:
# n_terms = 10  # Change this to the number of terms you want
# result = fibonacci(n_terms)
# print(f"Fibonacci series with {n_terms} terms: {result}")



def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = 8
print("Fibonacci series up to", n, "terms:")
for i in range(n):
    print(fibonacci(i),end=" ")