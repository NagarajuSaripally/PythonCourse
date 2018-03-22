# Print Hello World

def myFirstMethod():
	print("Hello World!")

myFirstMethod();


# Print Hello with passed name

def wish(name):
	print(f"Hello {name}")

wish("Raj")

# Simple Boolean, if passed value is true return true otherwise return false

def isBoolean(value):
	if value == True:
		return True
	elif value == False:
		return False

print(isBoolean(True))

#Using booleans, pass three arguments, if last argument is true pass first argument otherwise pass second argument

def trueParameter(x,y,z):
	if z == True:
		return x
	elif z == False:
		return y

print(trueParameter('x', 'y', True))

#simple math, pass two numbers and return some those numbers

def sum(num1, num2):
	return num1 + num2

print(sum(3, 6))

# simple comparison, pass two numbers, if first param is greater than second return True otherwise return False
def isGreater(num1, num2):
	if num1 > num2:
		return True
	else:
		return False

print(isGreater(3.1, 9))

# simple math, find passed argument is even number or not
def isEven(num):
	if num%2 == 0:
		return True
	else:
		return False

print(isEven(20))
