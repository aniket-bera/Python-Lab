fp = open("F:\BTech\PYTHON LAB\Demo3.txt", "w")

t = int(input("How many terms? "))

n1, n2 = 0, 1
count = 0

if t <= 0:
    print("Please enter a positive integer!!!", file = fp)

elif t == 1:
    print("Fibonacci series upto ", t, ": ", n1, file = fp)

else:
    while count < t:
        print("", n1, file = fp)
        nt = n1 + n2
       
        n1 = n2
        n2 = nt
        count += 1

fp.close()