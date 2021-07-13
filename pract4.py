'''2 Write a function calledfizz_buzzthat takes a number.If the number is divisible by 3, it should return “Fizz”.
If it is divisible by 5, it should return “Buzz”.If it is divisible by both 3 and 5, it should return “FizzBuzz”.
Otherwise, it should return the same number'''

def fizz_buzz():

    if num%3 == 0:

        return 'Fizz'
    elif num%5 == 0:

        return 'Buzz'
    elif num%3==0 and num%5==0:

        return 'FizzBuzz'
    else:
        return num

num = int(input("Enter a number:"))

fizz_buzz()
ans = fizz_buzz()
print(f"{ans}")
