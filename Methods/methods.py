'''
Methods in built in objects:

Some of them are:

for lists:  append(), pop() etc

How we can discover our own: help(list.insert). --> in jupitor editor : Shift + tab

built in help function: help(...)

3) options: docs.python.org : Python Standard Library.

syntax of defining the function:

def name_of_function():
	docstring explians function.
	print("Hello world!");
'''

'''
We can add defaults to the parameters in the function to avoid errors
'''
def say_hello(name='Doe'):
	print(f'Hello {name}')

say_hello();

print('\n')

def add_function(num1, num2):
	'''
	DOCSTRING : sum of the function:
	INPUT : two integers num1 and num2
	OUTPUT : sum of two Integers
	'''
	return num1 + num2

result = add_function(5,9)

print(f'sum of 5, 9 is : {result}')

print('\n')

# find out if the word dog is in the string

def dog_check(dogString):
	return 'dog' in dogString.lower()

print(dog_check("my dog name is peter"))