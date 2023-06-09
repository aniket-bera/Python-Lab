from math import pi

class Circle:
    radius = 0

    def __init__(self,r):
        self.radius = r
    
    def get_radius(self):
        return self.radius
    
    def calc_area(self):
        area = pi * self.radius**2
        return area

class Cylinder(Circle):
    height = 0
    
    def __init__(self,h):
        self.height = h
        super().__init__(r)
    
    def Calc_area(self):
        area = 2 * pi * self.radius * h
        return area

r = eval(input("Enter radius of circle: "))
ob1 = Circle(r)
print("Area of circle =", ob1.calc_area())
h = eval(input("Enter height of cylinder: "))
ob2 = Cylinder(h)
print("Area of curve surface of cylinder =", ob2.Calc_area())