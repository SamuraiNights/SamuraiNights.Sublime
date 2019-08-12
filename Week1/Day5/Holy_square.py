#import#
import time
#title#
print(" ")
print("Calculation of the Holy Square of Zupercat")
print(" ")
#definitions#
def loading_vertical():
	time.sleep(1)
	print(".")
	time.sleep(1)
	print(".")
	time.sleep(1)
	print(".")
	time.sleep(2)
	print("Done")
	time.sleep(2)
	print(" ")
def get_number_from_user(input_from_user):
	a = 0
	while True:
		a = input(input_from_user)
		if a.isdigit():
			break
	return a
def pythagoras_calculation_third_side(a,b):
	sum_c = int(a)**2 + int(b)**2
	third_side = sum_c**(1/2)
	return third_side
def square_calculation(third_side):
	square = third_side * third_side
	return square
def print_holy_square(a,b,third_side,holy_square):
	print("From the Magical Triangle of Doom with sides",str(first_num),"and",str(second_num) + ", there lies the Holy Square of Zupercat with equal sides of",str(third_side_var),"and an area of",str(square_calculation_var) + ".")
#Code#
first_num = get_number_from_user("Type a number for the first side of the Magical Trangle of Doom: ")
second_num = get_number_from_user("Type a number for the second side of the Magical Trangle of Doom: ")
third_side_var = pythagoras_calculation_third_side(first_num,second_num)
square_calculation_var = square_calculation(third_side_var)
print(" ")
time.sleep(2)
print("Calculating the Magic Kingdom of the Triangle and Square...")
loading_vertical()
print_holy_square(first_num,second_num,third_side_var,square_calculation_var)
