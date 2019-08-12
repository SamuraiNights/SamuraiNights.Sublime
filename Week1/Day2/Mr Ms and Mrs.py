print("Proper name remover :)")
name_lol = input("What's Your Name? (please put Mr. ,Ms. ,Dr. or Mrs. )(With space after them)")
proper_name = name_lol[0:4]
name = name_lol[4:]

if proper_name == "Mrs. ":
	proper_name = name_lol[0:5];
	print("Your improper name is" + name)

else:
	print("Your improper name is " + name);
