n = int(input("Enter a number:"))

length = len(str(n))
temp = n
sum =0

while n > 0:
    digit = n%10
    sum+= digit**length
    n //=10

if sum == temp:
    print("Armstrong")
else:
    print("Not Armstrong")
