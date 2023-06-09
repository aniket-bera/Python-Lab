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

r = eval(input("Enter radius of circle: "))
ob1 = Circle(r)
print("Area =", ob1.calc_area())