class Student:
	roll = 0
	rollNumber = "IMT20190"
	def __init__(self, name):
		Student.roll += 1
		self.rollNumber += str(self.roll)

