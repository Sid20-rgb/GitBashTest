'''Write a python program to check whether the number is Armstrong number or not using function:
[Hint: 153 - 1*1*1 + 5*5*5 + 3*3*3]'''

def armstrong():
    num = int(input("Enter the number:"))
    length = len(str(num))
    copy_num = num
    sum = 0

    while num > 0:

        digit = num%10
        sum += digit**length
        num = num//10

    if sum == copy_num:
        print("Armstrong number")

    else:
        print("Not an Armstrong number")

armstrong()