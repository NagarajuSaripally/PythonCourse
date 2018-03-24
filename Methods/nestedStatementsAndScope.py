'''
Scope is LEGB rule:

Local: Names assigmned in any way with in a function
E: Enclosing function locals : Names in the local scope of any and all enclosing function
Global : Names assigned at the tope-level of a module file or declared ina def with in the file:
B : Built-in  - Names preassigned in the built in names module: open, range, syntax error
'''

name = 'This is a global String'

def greet():
	name = "Sammy"
	def hello(): 
		print("hello " + name)

	hello()

greet()

print(name)


'''
if we use global keyword, if we change any local scope that impacts the global scope:
'''


x = 50

def func():
	global x
	print(f'X is {x}')

	x = 200

	print(f'Hey I am locally changed {x}')

func()
print(f'Global X is {x}')