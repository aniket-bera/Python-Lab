from math import pi

r = eval(input("Enter radius of a circle: "))
a = pi * r * r
p = 2 * pi * r

if r < 0:
    print("Invalid input!!!")
else:
    print("Area of circle =", a)
    print("Perimeter of circle =", p)