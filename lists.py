#CREATIING LIST 

#x = [1 , 'hello',(3+2j)]
#print(x)#....output will show the contents in above square bracket

#print(x[2])#...this print will have output dislaying (3+2j) as it's index is 2.

#print(x[0:2])#....this print will have output displaying [1,hello]i.e from 0 to 1 cause :2 is not considered.


#MODIFYING THE LIST.

#x = [1,2,3]

#y = x 

#x[1] = 15  #Here we are changing the value of index's 2nd element which is originally 2.That is we are reasssigning a value

#print(x)  #The output for this print statement will be [1,15,3] and not[1,2,3] because of reassigning.

#print(y) #This print statement will to display [1,15,3]

#x.append(12)

#print(y) 
#Now after appending both print(y) and print(x) will display the modified list.
#print(x)

#Abive same thing will happen here too 
#y.append(8)

#print(x)
#print(y)

#USING (z)

x = [1,2,3]
y = x

z = x.append(12)

print(z) #This print statement will display output as NONE

print(y) #output is [1,2,3,12]

x = x + [9,10]

print(x) #output is[1,2,3,12,9,10]
print(y) #output is [1,2,3,12] due to the statement z = x.append

