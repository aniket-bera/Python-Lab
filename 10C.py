import math as m
x = eval(input("Enter a number: "))

try:
    r = m.sqrt(x)
    print("Square root of entered number:",r)
except:
    print("You enter negetive number!!!")