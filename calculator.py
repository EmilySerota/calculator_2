"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


#def decipher(calc_input):

while True:

	calc_input = input("enter the input: ")
	to_calculate = calc_input.split(" ")
	funct = to_calculate[0]
	
	if funct.isdigit():
		print("Start with arithmatic function!")

	elif funct == "+":
		if len(to_calculate) == 3:
			num1 = float(to_calculate[1])
			num2 = float(to_calculate[2])
			print(add(num1,num2))
		else:
			print("Takes two numbers!")

	elif funct == "-":
		if len(to_calculate) == 3:
			num1 = float(to_calculate[1])
			num2 = float(to_calculate[2])
			print(subtract(num1, num2))
		else:
			print("Takes two numbers!")

	elif funct == "*":
		if len(to_calculate) == 3:
			num1 = float(to_calculate[1])
			num2 = float(to_calculate[2])
			print(multiply(num1, num2))
		else:
			print("Takes two numbers!")

	elif funct == "/":
		if len(to_calculate) == 3:
			num1 = float(to_calculate[1])
			num2 = float(to_calculate[2])
			print(divide(num1, num2))
		else:
			print("Takes two numbers!")

	elif funct == "square":
		if len(to_calculate) == 2:
			num1 = float(to_calculate[1])
			print(square(num1))
		else:
			print("Takes one number!")

	elif funct == "cube":
		if len(to_calculate) == 2:
			num1 = float(to_calculate[1])
			print(cube(num1))
		else:
			print("Takes one number!")

	elif funct == "pow":
		if len(to_calculate) == 3:
			num1 = float(to_calculate[1])
			num2 = float(to_calculate[2])
			print(pow(num1,num2))
		else:
			print("Takes two numbers!")

	elif funct == "mod":
		if len(to_calculate) == 3:
			num1 = float(to_calculate[1])
			num2 = float(to_calculate[2])
			print(mod(num1,num2))
		else:
			print("Takes two numbers!")

	elif funct == "q":
		break
	else:
		print("Nope. Start with an operator or 'q'")



# -------------- test cases --------------
"""print(decipher("+ 1 2"))
print (decipher("- 10 5"))
print(decipher("* 2 3"))
print(decipher("/ 7 2"))
print(decipher("square 2"))
print(decipher("cube 3"))
print(decipher("pow 2 5"))
print(decipher("mod 10 3"))
print(decipher("q"))
"""

