class Circle():

	pi = 3.14



	"""docstring for Circle"""
	def __init__(self, radius=1):
		self.radius = radius

	def get_circumference(self):
		return self.radius * self.pi * 2

my_circle = Circle(30)

print(my_circle.pi)

print(f'Circumference of circle with radius 30 is -> {my_circle.get_circumference()}')
		