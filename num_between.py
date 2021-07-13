'''Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700
 (both included).'''

num = ""
while num > 1500 and num < 2700:
    if num%7== 0 and num%5 == 0:
        print("It is the one.")
    else:
        print("Its not")