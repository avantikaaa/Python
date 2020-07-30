"""
class Student:
	name = ""
	rollNumber = 0
	def __init__(self, name, rollNumber):
		self.rollNumber = rollNumber
		self.name = name
"""
from student1 import *
class Institute:
	students = []
	def __init__(self, student_list):
		self.students = student_list
	def isStudentOf(self, s):
		if (s in self.students):
			return True
		else:
			return False
	def isAddable(self, s):
		if (not s in self.students):
			return True
		else:
			return False
	def addStudent(self, s):
		self.students.append(s)
s1 = Student( "nikhil" , 60 )
s2 = Student( "Mudum"  , 13 )
s3 = Student( "C2"     , 2  )
s4 = Student( "Neelabh" , 58 )
IIITB = Institute([s1,s2,s3])
print(IIITB.isStudentOf(s1))

print(IIITB.isStudentOf(s4))
print(IIITB.isAddable(s4))
print(IIITB.addStudent(s4))

for i in IIITB.students:
  print i.name,i.rollNumber
