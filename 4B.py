t = int(input("How many terms? "))

n1, n2, count = 0, 1, 0

if t <= 0:
    print("Please enter a positive integer!!!")

elif t == 1:
    print("Fibonacci series upto {}: {}".format(t, n1))

else:
    while count < t:
        print("Fibonacci series term {} is: {}".format(count+1, n1))
        nt = n1 + n2
        n1 = n2
        n2 = nt
        count += 1