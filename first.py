num = int(input("Enter a number:"))
even = 0
odd = 0

for x in range(1, num):
    if x%2== 0:
        even+=1
    else:
        odd+=1

print(even)
print(odd)
