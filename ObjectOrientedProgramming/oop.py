"""
Allows us to created our own objects and classes
Allows the code that is repeatable and organized

The basic way of creating object is using class

syntax : 

class NameOfClass():   name of the class should start with upper case

def __init__(self, param1, param2): // this is objets method to use elsewhere
	self.param1 = param1 // 
	self.param2 = param2

def some_method(self):
	print(self.param1)
"""

# __init__ method helps the instances of the classes

# self represents the instances of the Object itself

# attributes, we take in the argument, assign it using self.attribute

class Dog():

	#CLASS OBJECT ATTRIBUTE
	# SAME FOR ANY ISTNACE OF A CLASS

	species = 'mammal'

	def __init__(self, breed, name, spots ):
		#Expecting to string
		self.breed = breed
		#Expecting to be a string
		self.name = name
		#Expecting to be a boolean
		self.spots = spots

	def bark(self):
		print(f'Woof! My name is {self.name}')
	

# instance of sample: my_sample = Sample()

# my_dog = Dog(breed='Lab', name='samee', spots=True) --> if we don't pass anything we will get an error

# my_dog = Dog(breed='Lab')

#type(my_dog) --> __main__.Dog

my_dog = Dog('Lab', 'Frankie', True)

my_dog.bark()