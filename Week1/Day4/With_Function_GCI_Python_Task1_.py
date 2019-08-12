#title#
print("GCI Task 1 (Beginners)")
#function_definitions#
def get_integer_from_user():
	a = 0
	while True:
		a = input("Type a number: ")
		if a.isdigit():
			break
	return int(a)
def factorial_calculation_and_print_it(a):
	a = int(a)
	r = 1
	for c in range(1,int(a)+1,1):
		r = r*c
	print("Your Answer is: " + str(r))
#code_with_functions#
qwerty = get_integer_from_user()
#You can put this code --> print(type(qwerty)) <-- in this line to make sure you have an integer
factorial_calculation_and_print_it(qwerty)


