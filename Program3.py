# WRITE A PYTHON FUNCTION TO MULTPLY ALL THE NUMBERS IN A LIST.

#functiom for multiples in a list
def multiple(numbers):
    total = 1
    for num in numbers:
        total *= num
    return total
list = [1, 2, 3, 4, 5]
result = multiple(list)
print(result)  
