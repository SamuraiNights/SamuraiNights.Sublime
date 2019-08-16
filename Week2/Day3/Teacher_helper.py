import math

result = ""
dictionary = {}
all_keys = ""
best_score = 0
worst_score = math.inf
best_score_name = ""
worst_score_name = ""
a = []
for i in range (1,51,1):
	print(" ")
print("Welcome to 'Let Zupercat humiliate you haha' by Zupercat.Co.Ltd")
while True:
	user_answer = input("Enter your name and your score with a comma between them (press the 'spacebar' and press 'enter' when you have finished): ")
	if user_answer == " ":
		break
	temp_user_answer_list = user_answer.split(",")
	if int(temp_user_answer_list[1]) > best_score:
		best_score = int(temp_user_answer_list[1])
	if int(temp_user_answer_list[1]) < worst_score:
		worst_score = int(temp_user_answer_list[1])
	user_answer_list = user_answer.split(",")
	dictionary[user_answer_list[0]] = user_answer_list[1]
for key in dictionary:
	all_keys += key + ", "
	if int(dictionary[key]) == best_score:
		best_score_name += key + ", "
	if int(dictionary[key]) == worst_score:
		worst_score_name += key + ", "
	a.append(int(dictionary[key]))
dictionary_length = len(dictionary)
print(str(dictionary_length) + " student(s) completed the test: " + all_keys[:-2] + ".")
print("High score of: " + str(best_score) + ", by " + best_score_name[:-2] + ".")
print("Low score of: " + str(worst_score) + ", by " + worst_score_name[:-2] + ".")
avg = sum(a)/int(dictionary_length)
print("Average score of: " + str(round(avg,2)) + ".")