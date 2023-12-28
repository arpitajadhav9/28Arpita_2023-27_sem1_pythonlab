#TO DEMONSTRATE DIFF METHODS OF LISTS...

#STEP1: CREATION OF LIST.
x = [1 ,'hello' , (3+5j) , 56 , 'sakshi' ]

# ADDITION OF SINGLE ELEMENT IN LIST..
x.append(12)
print(x)

# ADDITION OF MANY ELEMENTS IN A LIST..
x.extend(['yashika','arpita',90])
print(x)

# METHOD TO REMOVE DEFAULT LAST ELEMENT FROM THE LIST..
x.pop(3)
print(x) #OUTPUT IS DISPLAYED BY EXCLUDING THE 3RD ELEMENT WHICH IS 56.

# TO REVERSE A LIST..
x.reverse()
print(x)

# TO INSERT AN ELEMENT IN AN SPECIFIC INDEX NUMBER:
x.insert(3,56)
print(x)

#TO SORT 

y = [15,14,13,12,11]
y.sort() #to sort it in ascending order.
print(y)
y.sort(reverse = True) # to sort it in descending order.
print(y)