#defining function
def sum():
    a = int(input("Enter a number:"))      #Here function itself is asking for values and adding by itself. main functions aren't giving their values.
    b = int(input("Enter a number:"))

    add = a + b

    print(f"The sum of two number is {add}.")
#calling function
sum()
print("Again")
sum()