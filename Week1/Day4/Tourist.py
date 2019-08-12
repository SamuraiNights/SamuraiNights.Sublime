print("Hello and welcome to the ultimate tourist sentence generator (beta-mode)!") 
print("Please read everything carefully...")
result = ""
city = input("The infamous Zupercat wants you to enter a city name: ")
country = input("Now, the super Zupercat orders you to enter the the name of the coutry that contains the city you just entered: ")
attract = input("Enter an attraction (press the 'spacebar' and press 'enter' when you have finished): ")
if attract == " ":
	print ("Welcome to",city + ",",country + ". There are many attractions but you didn't give me any...so...yeah.")
else:
	result += attract
	while True:
		attract = input("Enter an attraction (press the 'spacebar' and press 'enter' when you have finished): ")
		if attract == " ":
			break
		result += ", " + attract

	print ("Welcome to",city + ",",country + ". There are many attractions here, such as " + result + ".")