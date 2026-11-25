# Python program to find the
# factorial of a number
# provided by the user
def factiterative(n):
    factorial = 1
    if n != 0:
        for i in range(1,n + 1):
            factorial = factorial*i    
    return factorial


# take input from the user
num = int(input("Enter a number: "))


# check if the number is negative
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
else:
   f = factiterative(num)
   print("The factorial of",num,"is",f)
