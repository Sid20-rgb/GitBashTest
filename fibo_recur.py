def fibonacci(num):
    if n == 1:
        return 1
    elif n == 0:
        return 0

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter a number:"))

for i in range(n):

    print(fibonacci(i), end = " ")