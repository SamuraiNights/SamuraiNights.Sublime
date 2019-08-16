#imports#
import random
import time

#title#
print(" ")
print("Welcome to Ultra Hard Mode of Guess My Number! You are the lucky one chosen by The Almighty Zupercat. Please guess a number from (1-10) to (11-20)! You have five chances to guess this right, or else you will be thrown into Zupercat's Dungeon of Boredom and Chattering")
print(" ")
print("Now it's time to...... GUESS MY NUMBER!")
print(" ")
print(" ")
#code#
chance_holder = 0
correct_answer_1 = 0
correct_answer_2 = 0
correct_answer_1 = random.randint(1,10)
correct_answer_2 = random.randint(11,20)
correct_answer = random.randint(correct_answer_1,correct_answer_2)

for chance_holder in range(1,6,1):
	user_number = 0
	while True:
		user_number = input("please enter a guess: ")
		if user_number.isdigit():
			break
	user_number = int(user_number)
	if user_number == correct_answer:
		print("You're correct! Zupercat congratulates you with...... Her 'gratitude'!")
		break
	elif user_number == 1234567890:
		print("You have entered Zupercat's password for her dungeon.")
		time.sleep(2)
		print("You may enter without charges.")
		time.sleep(2)
		print(":D")
		time.sleep(2)
		break
	elif user_number == random.randint(61,68):
		print("You have entered the ever-changing password for Zupercat's Super-secret, Super-secure, No-chance-of-escaping Solitary Dungeons of Boredom and Death.")
		time.sleep(2)
		print("Entering it is free and compulsory for you...")
		time.sleep(2)
		break
	elif user_number == 6060:
		print("These are the coordinates for Zupercat's death pit.")
		time.sleep(2)
		print("You have been teleported there automatically.")
		time.sleep(2)
		print("You lost because you died.")
		time.sleep(2)
		break
	elif user_number == 57:
		print(":D Zupercat says nothing even though you entered Zupercat's favourite numbers.")
		break
	elif user_number == 1053:
		print(":D Zupercat says you lose for no apparent reason.")
		break
	elif user_number == 306:
		print("These are interesting coordinates. You have been teleported there automatically.")
		time.sleep(2)
		print("It's for the Sun.")
		time.sleep(2)
		print("You lost because you died.")
		time.sleep(2)
		break
	elif user_number == 123:
		print("You have lost a chance.")
		time.sleep(2)
		print("Zupercat laughs triumphantly.")
		time.sleep(2)
		print("lolz.")
		time.sleep(2)
		break
	elif user_number == 911:
		print("You have called the Zupercat police station.")
		time.sleep(2)
		print('Zupercat replies with ":D".')
		time.sleep(2)
		print("You have been arrested under Zupercat's Zuper orders.")
		time.sleep(2)
		break
	elif user_number == 110:
		print("You have called the Zupercat grammar police station.")
		time.sleep(2)
		print('You said: "Hllo"')
		time.sleep(2)
		print('Zupercat replies with ":D".')
		time.sleep(2)
		print("You have been arrested under Zupercat's grammar orders.")
		time.sleep(2)
		break
	elif user_number == random.randint(25,50):
		print("You have entered a number from 25 to 50.")
		time.sleep(2)
		print('Zupercat replies with "...".')
		time.sleep(2)
		print("Nothing happens.")
		time.sleep(2)
		break
	elif chance_holder == 5:
		print("You're wrong! The answer is",str(correct_answer) + ". Zupercat laughs at you for losing!")
		break
	elif user_number > correct_answer_2:
		print("Hmmm, that number is invalid because it's bigger than the biggest number possible. Zupecat laughs obnoxiously.")
	elif user_number < correct_answer_1:
		print("Hmmm, that number is invalid because it's smaller than the smallest number possible. Zupecat laughs obnoxiously.")
	else:
		print("Nope! Zupercat smirks at you.")

