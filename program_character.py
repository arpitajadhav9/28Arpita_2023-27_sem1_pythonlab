#write a program that forms a list of first character of every word in another list



mylist=['flower','stone','tree','bird']

charlist=[]

for word in mylist:
    charlist.append(word[0])

print(charlist)