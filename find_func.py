# FIND () IS A FUNCTION
# STR.FIND()

str='ITM SKILLS UNVERSITY'
print(str.find('I'))# output is 0 cause I starts from index number 0 
print(str.find('ITM')) # output is 0 cause ITM starts from index number 0 
print(str.find('SKILL',1)) # outpt is 4 because skill word indedx number is 4 and 1 is written because it will start searching skill from index number 1 
print(str.find('SKILLS',1,18)) #  OUTPUT IS 4 cause it will check from index number 1 to 18 if there is present skills and then it will display output as four cause skills starts from index number 4
print(str.find('SKILLS',1,3)) # output is -1 cause from index number 1 to 3 there is no skills written so it will display -1 cause skills starts from index number 4