class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def Display(self):
        print("X & Y co-ordinates are: (", self.x, ",", self.y, ")" )
    
    def Translate(self,x,y):
        self.x += y
        self.y += x

x, y = [int(i) for i in input("Enter X & Y co-ordinates: ").split(",", 1)]
ob1 = Point(x, y)
ob1.Display()
print("\nAfter translate X & Y:")
ob1.Translate(x, y)
ob1.Display()