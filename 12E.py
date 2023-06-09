class Shape:
    color =""
    
    def __init__(self,c):
        self.color = c

class Rectangle(Shape):
    lenght = 0
    breadth = 0
    
    def __init__(self,c,l,b):
        self.length = l
        self.breadth = b
        super().__init__(c)
    
    def calc_area(self):
        area = self.length * self.breadth
        return area
    
    def Rect_details(self):
        print(self.lenght, self.breadth, self.color)
        print(self.calc_area())

class Triangle(Shape):
    base = 0
    height = 0
    
    def __init__(self,c,b,h):
        self.base = b
        self.height = h
        super().__init__(c)
    
    def calc_area(self):
        area = 0.5 * self.base * self.height
        return area
    
    def Tring_details(self):
        print(self.base, self.height, self.color)
        print(self.calc_area())

c = ""
l = eval(input("Enter length of rectangle: "))
b = eval(input("Enter breadth of recctangle: "))
ob1 = Rectangle(c, l, b)
print("Area of rectangle =", ob1.calc_area())
c = ""
b = eval(input("Enter base of triangle: "))
h = eval(input("Enter height of triangle: "))
ob2 = Triangle(c, b, h)
print("Area of triangle =", ob2.calc_area())