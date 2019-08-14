for i in range(0,50,1):
	print(" ")
print("Hi!")
print(" ")
user_word = input("Word Please: ")
print(" ")
result = ""
for i in range(len(user_word)):
	if user_word[i].isupper() == True:
		result += user_word[i].lower()
	elif user_word[i].islower() == True:
		result += user_word[i].upper()
	else:
		result += user_word[i]

print(result)