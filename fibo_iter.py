def fibo(n):
    a = 0
    b = 1
    print(a, b , end = " ")
    for i in range(n):
        c = a + b
        a = b
        b = c
        print(c, end = " ")

n = int(input("Enter a number:"))

fibo(n)

