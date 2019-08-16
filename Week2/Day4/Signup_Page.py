for i in range(1,101,1):
	print(" ")
print("Sign up to Zupercat.Co.Ltd's Fabrik Page")
print(" ")
dictionary = {}
name = input("Tell me your name or else Zupercat will take all your sandwiches that you will eat in your life --> ")
print(" ")
email = input("Hello " + name + "! Now, tell me your E-mail or you will be thrown in the worst dungeons of Zupercat (Earth's Core)--> ")
print(" ")
live = input("Lastly, tell me where you live, so we could attack you with glitter and boredom whenever we want. If you don't tell me, then you will suffer from Zupercat taking your lunch --> ")
print(" ")
print("Thanks for the information! Zupercat is happy that you obeyed. She now asks you which information you want to see...")
print(" ")
dictionary = {"Name":name,"Email":email,"Live":live}
print("(Name,Email, Live or change email (press space and then enter to stop))")
show_info = input("")
print(" ")
chance = 0
while True:
	show_info = show_info.lower()
	show_info = show_info.split()
	show_info = ''.join(show_info)
	if show_info == "name":
		print("Zupercat searches the data files... Your name is " + name + ".")
		print(" ")
		print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
		print("(Name,Email or Live (press space and then enter to stop))")
		show_info = input("")
		print(" ")
		show_info = show_info.lower()
	elif show_info == "email":
		print("Zupercat looks on her Zuper-computer's Zuper-files for Zuper-info on your E-mail... Your E-mail is " + email + ".")
		print(" ")
		print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
		print("(Name,Email or Live (press space and then enter to stop))")
		show_info = input("")
		print(" ")
		show_info = show_info.lower()
	elif show_info == "live":
		print("Zupercat looks at her Attack files and finds your location files inside... You live in " + live + ".")
		print(" ")
		print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
		print("(Name,Email or Live (press space and then enter to stop))")
		show_info = input("")
		print(" ")
		show_info = show_info.lower()
	elif show_info == "changeemail":
		print("Zupercat looks at your E-mail... Your E-mail is currently this: " + email)
		print(" ")
		print("Please enter your new E-mail: ")
		email = input("")
		print(" ")
		print("Your E-mail has been changed.")
		print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
		print("(Name,Email or Live (press space and then enter to stop))")
		show_info = input("")
		print(" ")
		show_info = show_info.lower()
	elif show_info == "":
		print("Thanks for using Fabrik by Zupercat.Co.Ltd. See you next time.")
		break
	elif (show_info != "name" or show_info != "email" or show_info != "live") and chance == 0 and show_info != "":
		print("I'm afraid Zupercat cannot show that. She hisses angrily and says if you do it again, she will come attack you.")
		print(" ")
		print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
		print("(Name,Email or Live (press space and then enter to stop))")
		show_info = input("")
		print(" ")
		show_info = show_info.lower()
		chance += 1
	elif chance >= 1 and show_info != "":
		print(" ")
		print('Zupercat says: "Uggghhhh!" and she scratched you. You are now banned from this website.')
		break
