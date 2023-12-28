# WAP THAT DEFINES LIST OF COUNTRIES THAR ARE A MEMBER OD BRICS.CHECK WHETHER THE COUNTRIES ARE MEMBER OF BRICS OR NOT

countries = ["india", "russia", "srilanka", "china", "brazil"]

member = input("Enter the name of the country: ").lower() #it will make the input in lower case whether it is written in capital aur small form.

if member in countries:
	print(member, " is the member of BRICS")
else:
	print(member, " is not a member of BRICS")