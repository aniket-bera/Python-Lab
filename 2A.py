a = input("Enter value of A: ")
b = input("Enter value of B: ")

#using 3rd variable
temp = a
a = b
b = temp
print("After 1st swapping:\nA =", a, "\nB =", b)

#without using 3rd variable
a,b = b,a
print("After 2nd swapping:\nA =", a, "\nB =", b)