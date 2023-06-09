first = int(input("Enter first number = "))
last = int(input("Enter last number = "))

print("Prime numbers range {} to {} are:".format(first, last))

for i in range(first, last + 1):
   temp = 0
   for j in range(2, (i//2)):
       if i % j == 0:
           temp += 1
           break
   if temp == 0 and i > 1:
        print(i)