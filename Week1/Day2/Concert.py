print("Hi, my goal is to not let you go to the Music Concert called The Show of a Century.")
name=input("What's your name? ")
money=input("Ok, I don't care but how much money do you have?(Please input a number) $")
will_rain=input("Will it rain tonight?(Yes or No) ")
ben_going=input("Is your friend Boris The Animal going?(Yes or No) ")
jon_going=input("Is Your friend John Snow going?(Yes or No) ")
friend_going= ben_going == "Yes" or jon_going == "Yes"
if int(money) > 50 and will_rain == "No" and friend_going:
	print("Yes you can go to the Concert but don't be too happy because weather can always change...");
else:
	print("Aha! No, you cannot and will never go to the Concert. Muahahahahahahaaa!!!")