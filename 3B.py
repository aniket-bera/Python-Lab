import math

a = int(input("Enter value of a = "))
b = int(input("Enter value of b = "))
c = int(input("Enter value of c = "))

dis = (b ** 2) - (4 * a * c)

if a == 0:
    print("Invalid input!!!")

else:
    if dis > 0:
        print("Roots are real and different:")
        print((-b + math.sqrt(dis)) / (2 * a))
        print((-b - math.sqrt(dis)) / (2 * a))
        
    elif dis == 0:
        print("Roots are equal and real:")
        print((-b) / (2 * a))
    
    else:
        print("Roots are distinct complex:")
        print((-b) / (2 * a), "+", math.sqrt(-dis) / (2 * a))
        print((-b) / (2 * a), "-", math.sqrt(-dis) / (2 * a))