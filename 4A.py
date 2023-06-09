x = int(input("Enter the base: "))
n = int(input("Enter the power: "))

y = 1

for i in range(n):
    y = y * x

print("Result =", y)