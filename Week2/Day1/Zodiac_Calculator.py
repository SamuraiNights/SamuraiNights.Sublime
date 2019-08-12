#imports#
import time
from PIL import Image
#definitions -->#
#zodiac calculating#
def calculate_zodiac(birth_year):
	year_of_zodiac = int(birth_year) % 12
	if year_of_zodiac == 1:
		a = "Rickety Rooster"
	elif year_of_zodiac == 2:
		a = "Dreamy Dog"
	elif year_of_zodiac == 3:
		a = "Pirate Pig"
	elif year_of_zodiac == 4:
		a = "Rambunctious Rat"
	elif year_of_zodiac == 5:
		a = "Outstanding Ox"
	elif year_of_zodiac == 6:
		a = "Terrific Tiger"
	elif year_of_zodiac == 7:
		a = "Rackety Rabbit"
	elif year_of_zodiac == 8:
		a = "Dreadful Dragon"
	elif year_of_zodiac == 9:
		a = "Sentient Snake"
	elif year_of_zodiac == 10:
		a = "Holly Horse"
	elif year_of_zodiac == 11:
		a = "Galvanising Goat"
	else:
		a = "Marvelous Monkey"
	return str(a)
#photo#
def open_photo(year_of_zodiac):
	if year_of_zodiac == "Rickety Rooster":
		im = Image.open("Zodiac_Photos/10Rooster.jpg")
		im.rotate(360).show()
	elif year_of_zodiac == "Dreamy Dog":
		im = Image.open("Zodiac_Photos/11Dog.jpg")
		im.rotate(360).show()
	elif year_of_zodiac == "Pirate Pig":
		im = Image.open("Zodiac_Photos/12Pig.jpg")
		im.rotate(360).show()
	elif year_of_zodiac == "Rambunctious Rat":
		im = Image.open("Zodiac_Photos/1Rat.jpg")
		im.rotate(360).show()
	elif year_of_zodiac == "Outstanding Ox":
		im = Image.open("Zodiac_Photos/2Ox.jpg")
		im.rotate(360).show()
	elif year_of_zodiac == "Terrific Tiger":
		im = Image.open("Zodiac_Photos/3Tiger.jpg")
		im.rotate(360).show()
	elif year_of_zodiac == "Rackety Rabbit":
		im = Image.open("Zodiac_Photos/4Rabbit.jpg")
		im.rotate(360).show()
	elif year_of_zodiac == "Dreadful Dragon":
		im = Image.open("Zodiac_Photos/4Dragon.jpg")
		im.rotate(360).show()
	elif year_of_zodiac == "Sentient Snake":
		im = Image.open("Zodiac_Photos/6Snake.jpg")
		im.rotate(360).show()
	elif year_of_zodiac == "Holly Horse":
		im = Image.open("Zodiac_Photos/7Horse.jpg")
		im.rotate(360).show()
	elif year_of_zodiac == "Galvanising Goat":
		im = Image.open("Zodiac_Photos/8Goat.jpg")
		im.rotate(360).show()
	else:
		im = Image.open("Zodiac_Photos/9Monkey.jpg")
		im.rotate(360).show()
#<-- definitions#
#spaces for the start#
for i in range(1,50,1):
	print(" ")
#title#
print("Welcome to the Almighty Zodiac Calculator of Doom!")
print(" ")
#input#
while True:
	birth_year = input("Enter a birth year: ")
	if birth_year.isdigit():
		break
#print "calculating"#
time.sleep(1)
print(" ")
print("Calculating...")
print(" ")
#result#
zodiac = calculate_zodiac(birth_year)

time.sleep(1.5)
print("You're The " + zodiac + "!")
print(" ")
time.sleep(1.5)
print("Opening photo of The",zodiac,"...")
print(" ")
print("Displaying photo of The",zodiac,"...")
print(" ")
time.sleep(2)
open_photo(zodiac)