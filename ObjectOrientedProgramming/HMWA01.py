"""
Fill in the Line class methods to accept coordinates s a pair of tuples and return the slope and distance of the line.

coordinates1 = (3,2)
coordinates2 = (8,10)

li.distance() --> 9.433981132056603
li.slope() --> 1.6

"""

class Line():

	def __init__(self, cord1, cord2):
		self.cord1 = cord1
		self.cord2 = cord2

	def distance(self):
		x1,y1 = self.cord1
		x2,y2 = self.cord2

		return ((x2-x1)**2 + (y2-y1)**2)**0.5

	def slope(self):
		x1,y1 = self.cord1
		x2,y2 = self.cord2

		return (y2-y1)/(x2-x1)


li = Line((3,2), (8,10))

print(f"The distance of given coordinates (3,2) and (8,10) is --> {li.distance()}")

print(f"The slope of given coordinates (3,2) and (8,10) is --> {li.slope()}")


"""
Find the voulme and surface area of a cylinder with given height and radius
"""

class Cylinder():

	def __init__(self, height=1, radius=1):
		self.height = height
		self.radius = radius
		self.pi = 3.14

	def surfaceArea(self):
		return ( (2 * self.pi * self.radius * self.height) + (2 * self.pi * (self.radius ** 2)))

	def voulme(self):
		return self.pi * (self.radius ** 2) * self.height


c = Cylinder(2,3)


print(f"The surface area of given given cylinder with height, radius (2, 3) is --> {c.surfaceArea()}")

print(f"The voulme of given given cylinder with height, radius (2, 3) is --> {c.voulme()}")