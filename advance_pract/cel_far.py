'''2.Write a Python program to convert temperatures to and from celsius, fahrenheit.C = (5/9) * (F -32)'''


choice = int(input("Celsius(c) or Fahrenheit(f):"))

if choice == 2:
    F = int(input("Enter Fahrenheit:"))

    C = (5/9) * (F-32)

    print(f"The converted celsius is {C}.")

else:
    C = int(input("Enter Celsius."))

    F= (C * 9)/ 5 + 32

    print(f"The converted fahrenheit is {F}.")


