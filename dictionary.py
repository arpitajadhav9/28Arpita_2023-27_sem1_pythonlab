#are mutable

#d = { 1 : 'hello' , 'two' : 42 , 'blah' :[1,2,3]}
#print(d)

#d['blah']
#print(d['blah'])

#d[1]
#print(d[1])

#d['two']
#print(d['two'])
 
 # ADD/MODIFY THE DICTIONARY

 #modify

#print(d)

#d['two']=99
#print(d)

# add

#d[7] = 'new entry'
#print(d)

#to delete a element

#d = {1 :'hello', 2 : 'there ', 10 : 'world'}
#print(d)

#del(d[2])
#print(d)

# Copying dictionaries and lists

#l1 = [1] # value of l1 is [1]

#l2 = list(l1) #we assign value of l2 as value of l1 

#print(l1)
     #here output of both l1 and l2 will be [1]only
#print(l2)

#l1[0] = 22 # now here we assign value of l1 as 22


#print(l1) # now the output of l1 will show nnew assigned value as 22

#print(l2) # but when will see the output of l2 it will be [1] only if we write

#l2 = list(l1) #this copies the list of l1 and display it in output of l2
#print(l2) 


#COPYING 

d = {1:10}

d2 = d.copy()

print(d)

d[1]=22

print(d)

print(d2)


