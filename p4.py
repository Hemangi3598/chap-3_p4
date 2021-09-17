# wapp to read a year and find if its leap year

year = int(input("enter a year"))
if year < 0 :
	print("invalid year")
else:
	if year % 100 == 0 and year % 400 == 0:
		print("yes")
	elif year % 100 != 0 and year % 4 == 0 :
		print("yes")
	else:
	
		print("nopes its not a leap year")




# leap year comes after every 4 years if its not a century year
# leap year comes after every 400 years if its a century year