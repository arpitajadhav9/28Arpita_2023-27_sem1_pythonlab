#write a program that create a dictionaries of cube of odd number in range 1to10 in python

oddcubes = {}
for num in range(1, 11):
    if num % 2 != 0:  
        oddcubes[num] = num ** 3
print("Dictionary of Cubes of Odd Numbers:", oddcubes)