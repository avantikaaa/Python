class circle:
	radius = 0				#Attribute radius
	pi = 3.1415				#Static variable "pi"
	def area(self):				#Area of the circle - Radius is changed in the main code
		return circle.pi*self.radius*self.radius
	def circumference(self, radius):	#Circumference of the cirlce
		return 2*circle.pi*self.radius
class rectangle:
	length = 0				#Attributes length and breadth
	breadth = 0
	def area(self):
		return self.length*self.breadth
	def circumference(self):
		return 2*(self.length+self.breadth)

