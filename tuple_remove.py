# WAP TO REMOVE AN EMPTY TUPLES(s) FROM A LIST OF TUPLES.

a = [(),(),(""),('a','b'),('a','b','c'),('d')]
removetup= [t for t in a if bool(t)]
print("List of tuples without empty tuples:", removetup)