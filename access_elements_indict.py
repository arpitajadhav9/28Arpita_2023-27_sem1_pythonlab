#2.Wap for accessing elements from a dictionary.     i/p: r1={'id':101,'name':'Amit','Age':21}

 # a. By using key name.
# b. By using get() method.

my_dict = {1: "India", 'city': 'New Delhi', 'Record': {'id': 101, 'name': 'Amit', 'age': 21}}
for keys in my_dict.values():
    print("Key: ", keys)

all_values = list(my_dict.values())
for val in all_values:
    print("All Values using get():", val)