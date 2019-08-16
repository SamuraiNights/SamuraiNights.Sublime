#imports#
import time
#title#
for i in range (1,51,1):
	print(" ")
time.sleep(1)
print("Hello and welcome to Hangman of Doom by Zupercat.Co.Ltd!!!")
print(" ")
#player 1 input#
p1_input = input("Player 1, please enter a word (don't let Player 2 see): ")
for i in range (1,1001,1):
	print(" ")
#variables#
chance = 5
letters_remain = "abcdefghijklmnopqrstuvwxyz"
word = "_ "*len(p1_input)
p2_input = ""
p2_guess = ""
word_no_space = ""
i = 6
#code#
while True:
	i -= 1
	correct_test = 0
#check if guess is correct#
	if chance > 0:	
		print(" ")
		word = ""

		if p2_input in p1_input:
			correct_test += 1

		for j in range(len(p1_input)):
			if p1_input[j] in p2_guess:
				word += p1_input[j] + " "
			else:
				word += "_ "
		print("Word: " + word)
#letters that you have already enterec#
		if i < 5:
			letters_remain = letters_remain.replace(p2_input,"-")
		print("Letters remaining: " + letters_remain)
#check if guess is correct part 2#
		if correct_test <= 0:
			chance -= 1
#checking how many chances are left#
			print("Chances left: " + str(chance))
		elif correct_test > 0:
			print("Chances left: " + str(chance))
		word_no_space = ''.join(e for e in word if e.isalnum())
#win situation#
		if word_no_space == p1_input:
			print(" ")
			print("Above are your statistics :)")
			print(" ")
			print("You're correct! The answer is " + p1_input + "! Zupercat is bouyant with joy!")
			break
#guess a letter#
		while True:
			p2_input = input("Guess a letter: ")
			if len(p2_input) == 1:
				break
#lose situation#
		p2_guess += p2_input
		if chance == 0:
			print("You're wrong! The word is " + p1_input + "! Zupercat laughs boisterously at you for losing!")
			break
