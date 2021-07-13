'''1 Write a Python function to find the Max of three numbers'''
def num():
    if a > b and a > c:

        return a
    elif b > a and b>c:

        return b
    else:

        return c
a = int(input("Enter a number:"))
b = int(input("Enter a number:"))
c = int(input("Enter a number:"))

num()
max = num()

print(f"The max num is {max}.")


