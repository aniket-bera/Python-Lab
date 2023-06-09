n = input("Enter some numbers: ").split(',')
d = {}

for i in n:
    d[int(i)] = n.count(i)
print(d)