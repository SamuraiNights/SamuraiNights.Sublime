#title
print("GCI Task 1 (Beginners)")
#false_number_check
while True:
	a = input("Type a number: ")
	if a.isdigit():
		break
#answer
a = int(a)
r = 1
for c in range(1,a+1,1):
	r = r*c
print("Your Answer is: " + str(r))

