# EXPLANATION OF DICTIONARY IN MORE DETAIL
# - set of key-value pair 
# - are mutable.
# - ACTUAL USE IN DATABASE.
#- some content return befor colon(:) is key 
# - (,) is to separate one key-value pair from other key-value pair.
# 

 # d['blah'] - how to read this ====> list inside dictionray d.

d = {1 : 'hello', 'two':42 , 'blah': [1,2,3]}

print(d) # output - {1:'hello}

print(d['blah'])

print(d['blah'][1]) # This is the format to print single content of list from a key having its value as list inside a dictionary.

#TRY DICTIONARY INSIDE A DICTIONARY........



#DELETING ELEMENTS INSIDE THE DICTIONARY...
print(d)

del(d['two']) #this deletes the element 'two':42
print(d)  # this will display {1:'hello' , 'blah': [1,2,3]}


