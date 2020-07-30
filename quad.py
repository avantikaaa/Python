'''
import math
class parallelogram:
    print "In Paralleogram: "
    def __init__(self, side1, side2, angle):
        self.side1 = side1
        self.side2 = side2
        self.angle = angle
    def perimeter(self):
        return 2*(self.side1+self.side2)
    def area(self):
        height = math.sin(self.angle)*self.side1
        return height*self.side2
class rectangle(parallelogram):
    print "In Rectangle"
    def __init__(self, l, b):
        parallelogram.__init__(self, l, b, math.pi/2)
class rhombus(parallelogram):
    print "In Rhombus: "
    def __init__(self, l, angle):
        parallelogram.__init__(self, l, l, angle)
class square(rectangle, rhombus):
    print "In Square: "
    def __init__(self, l):
        rectangle.__init__(self, l, l)
        rhombus.__init__(self, l, math.pi/2)
s1 = square(1)
print math.sin(math.radians(37))
print s1.area(),
print s1.perimeter()
re1 = rectangle(4,5)
print re1.area(),
print re1.perimeter()
rh1 = rhombus(5, math.radians(74))
print "{0:.2f}".format(rh1.area()),
print rh1.perimeter()
'''
class Base: 
    def __init__(self): 
        self.a = "avantika"
        self.__c = "GeeksforGeeks"
        print self.a
        print self.__c
  
# Creating a derived class 
class Derived(Base): 
    def __init__(self): 
          
        # Calling constructor of 
        # Base class 
        Base.__init__(self)  
    #    print("Calling private member of base class: ") 
     #   print(self.__c) 
# Driver code 
obj1 = Base() 
print(obj1.a)

'''
obj2 = Derived()
print obj2.a
print obj2.__c
'''


