fp = open("F:\BTech\PYTHON LAB\Demo2.txt", "w")

lower = int(input("Enter lower value: "))
upper = int(input("Enter upper value: "))

print("Prime number between",lower,"to",upper,":", file=fp)
for n in range(lower, upper):
    for i in range(2, n):
        if(n%i == 0):
            value = []
            value.append(n)
            break
    else:
        print(n, end=' ', file = fp)

fp.close()