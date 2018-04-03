class Animal():
	def __init__(self):
		print("Animal Created")

	def who_am_i(self):
		print("I am an Animal")

	def eat(self):
		print("I am eating")

myAnimal = Animal()


class Dog(Animal):
	"""docstring for Dog"""
	def __init__(self):
		Animal.__init__(self)
		print("Dog Created")

	def eat(self):
		print("I am a dog and eating")

myDog = Dog()



"""
Polymorphism Exmaple
"""

class Animal1():
	def __init__(self, name):
		self.name = name

	def speak(self):
		raise NotImplementedError("Sub class must implement this abstract method")


class Dog1(Animal1):
	
	def speak(self):
		return self.name + " says woof!"

class Cat1(Animal1):
	
	def speak(self):
		return self.name + " says Meow!"


fido = Dog1("Fido")
fiddler = Cat1("Fiddler")

print(fido.speak())
print(fiddler.speak())