x = int (input ("Enter number of rows: "))

ascii = 65

for i in range (1, x + 1):
    for j in range (1, i + 1):
        print ("%c" % (ascii), end = " ")
    ascii += 1
    
    print ()