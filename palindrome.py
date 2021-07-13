n = int(input("Enter a number:"))

rev = 0
temp = n

while n>0:
    digit = n%10
    rev = rev*10+digit
    n //= 10

if rev == temp:
    print("Palindrome")
else:
    print("Not Palindrome")