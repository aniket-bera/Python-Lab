def automorphic(num):
    
    n = len(str(num))
    
    sqr = num**2
    
    last = sqr % (10**n)
    
    return last == num

start, end = [int(i) for i in input("Enter range of checking numbers: ").split("-", 1)]

for i in range(start, end + 1):
    if automorphic(i):
        print(i)