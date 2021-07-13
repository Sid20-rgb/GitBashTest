'''1. Write a program to print the multiplication of 3 using recursive. f(n)=3*n i.e multiple of 3.'''

def mul(n):
    if n == 1:
        return 3
    else:
        return 3 + mul(n-1)

n = int(input("Enter a number:"))
for i in range(n):
    ans = mul(n)
    print(f"{3}*{i} =")
    print(ans)


