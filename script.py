birth_year = input("Enter your year of birth:")
	
age = 2019 - int(birth_year)
    
print(age)
	
if  age < 18:
	     print( "you are a minor")
elif age >= 18 and age < 36:
	     print("you are a youth")
else:
	     print("you are and elder")

