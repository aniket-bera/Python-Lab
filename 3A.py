a = eval(input("Enter value of A: "))
b = eval(input("Enter value of B: "))
c = eval(input("Enter value of C: "))

if a >= b and a >= c:
   greatest = a

elif b>= a and b >= c:
   greatest = b

else:
   greatest = c

print("The greatest number:", greatest)