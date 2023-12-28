#1.Wap to create a dictionary with mixed keys, and 
   #  i print the keys, 
    # ii print values &
    # iii key-value pairs.   

my_dict = {1: "India", 'city': 'New Delhi', 'Record': {'id': 101, 'name': 'Amit', 'age': 21}}

keys = list(my_dict.keys())
for key in keys:    
    print("Keys:", key)

values = list(my_dict.values())
for value in values:
    print("Values:", value)

key_value_pairs = list(my_dict.items())
for keyval in key_value_pairs:  
    print("Key-Value Pairs:", keyval)