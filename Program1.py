# WRITE A PYTHON FUNCTIOON TO FIND THE MAXIMUM OF THREE NUMBERS.

#largest among three
def numbers(num1, num2, num3):
    return max(num1, num2, num3)
num1=int(input("Enter number 1:-"))
num2=int(input("Enter number 2:-"))
num3=int(input("Enter number 3:-"))
result = numbers(num1, num2,num3)
print(f"{result} is the largest number among three")

  