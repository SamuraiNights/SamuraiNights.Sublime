n=0
print("Welcome to Your World's Location Virtual Simulator")

while n == 0:
	a = input("Where do you want to go? (School, Mall or Gym) ")
	if a == "School":
		print("Ok, don't forget to bring homework for school and avoid Mr. Riches or Zupercat will make your detention worse than you could ever imagine!")
		n = 1
		break
	elif a == "Mall":
		print("Sure, but don't forget your Mom/Dad's credit card! You can ask Zupercat for a credit card if you really need it bur she will make you pay her back!")
		n = 1
		break
	elif a == "Gym":
		print("Aha, don't forget your shoes, water and shorts, or else Zupercat will punish you with eternal glitter, boredom and chattering!")
		n = 1
		break
	else:
		print("The Zupercat will only allow you to go to the Mall, School or Gym. Please choose again.")

