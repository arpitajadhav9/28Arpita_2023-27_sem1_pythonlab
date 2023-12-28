#PROGRAM TO FIND LCM OF ANY TWO USER ENTERED NUMBER.(using while loop)

p = x = int(input("Enter the 1st number: "))
q = y = int(input("Enter the 2nd number: "))

while x != y:
    if x > y:
        x = x - y
    else:
        y = y-x

    lcm  = (p*q)/x
    print("The LCM is:",lcm)    