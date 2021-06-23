def myfunc(x,y):
	return sum((x,y)) * 0.05

print(myfunc(40,50))

#if we wanna pass arbitory number of arguments --> means adding the parameters as they are coming -> as many as I want
#python takes all the arguments and place them in the tuples.
# * adding the parameter treats as argments, name doesn't matter only suffix * matters

def myfunc2(*args):
	print(args)

def myfunc3(*args):
	for item in args:
		print(item)

myfunc3(10,20,30,40,50,60)

#instead of printing the tuples, if we wanna key and value pairs like dictionaries, we can use **kwargs
# **kwargs --> keyword arguments

def myfunc4(**kwargs):
	if 'fruit' in kwargs:
		print(f'My fruit is :{kwargs["fruit"]}')
	else:
		print('I didnot find any fruit')

myfunc4(fruit='apple')
myfunc4(veggie='carrot')
myfunc4(fruit='banana', veggie='califlower')


def myfunc5(*args, **kwargs):
	print(f'I would like {args[0]} {kwargs["food"]}')

myfunc5(10,20,30,food='rice',fruit='mango',vehicle='accord')


def myfunc6(*args):
	return sum(args)

print(myfunc6(10,20,30,40))


def myfunc7(*args):
	return [num for num in args if num % 2 == 0]

print(myfunc7(10,9,8,37,45,44,32,24,28,49,47))

def myfunc8(string):
	my_string = ''
	for index,character in enumerate(string):
		if(index % 2 != 0):
			my_string += character.upper()
		else:
			my_string += character.lower()
	return my_string

print(myfunc8('JohnDoe'))
