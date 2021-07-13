#now we are using parameters to ask for the value
def sum(a,b):

    add = a + b
    print(f"The sum is {add}.")

c = int(input("Enter a number:"))      # '''main function in giving values from outside which is also called parameter.'''
d = int(input("Enter a number:"))
sum(c,d)
print("Again")
c = int(input("Enter a number:"))
d = int(input("Enter a number:"))
sum(c,d)
