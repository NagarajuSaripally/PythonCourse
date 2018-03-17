'''
Loops: iterate through the dataypes that are iterable, iterable datatypes in python or in any language

string, lists, tuples, dictionaries

keywords to iterate through these iterables:

#for

syntax

for list_item in list_items:
	print(list_item)
'''

# lists:

my_list_items = [1,2,3,4,5,6]

for my_list_item in my_list_items:
	print(my_list_item)

# strings

mystring = 'Hello World!'

for eachChar in mystring:
	print(eachChar)

#without assigning varibles

for variable in 'Good Morning':
	print(variable)

# here instead of each character, we can print what ever the string that we want many times as string length
# so instead of putting a variable name we can use _ there
for _ in 'Hello World!':
	print('cool!')

# tuples:

tup = (1,2,3)

for eachTup in tup:
	print(eachTup)


# Tuple unpacking, sequence contain another tuples itself then for will upack them

my_tuples = [(1,2),(3,4),(5,6),(7,8),(9,0)]

print("length of my_tuples: {}".format(len(my_tuples)))

for item in my_tuples:
	print(item)

# this is called tuple unpacking. techincally we don't need paranthesis like (a,b) it can be just like a,b
for (a,b) in my_tuples:
	print(a)
	print(b)


#dictionaries:

d = {'k1': 1, 'K2': 2, 'K3': 3}

for item in d:
	print(item)

for value in d.values():
	print(value)




'''
While loop, it continues to iterate till the condition satisfy
syntax:

while conition:
	# do something

while condition:
	# do something:
else:
	# do something else:
'''

x = 0

while x < 5:
	print(f'The current value of x is {x}')
	x += 1

while x < 10:
	print(f'The current value of x is {x}')
	x += 1
else:
	print('X is not should not greater than 10')



'''
useful keywords in loops
break, continue, pass

pass: do nothing at all
'''

p = [1,2,3]

for item in p:
	#comment
	pass # it just passes, in pythong for loops we need at least on statement in loop

print("Passed");


letter = 'something here'

for let in letter:
	if let == 'e':
		continue
	print(let)


for let in letter:
	if let == 'e':
		break
	print(let)