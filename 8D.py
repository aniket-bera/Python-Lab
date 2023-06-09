def matmult(m1,m2):
	c=[[0 for row in range(len(m1))]for col in range(len(m2[0]))]
	for i in range(len(m1)):
		for j in range(len(m2[0])):
			for k in range(len(m2)):
				c[i][j] += m1[i][k] * m2[k][j]
	return c

s1 = []
s2 = []

r1, c1 = [int(e) for e in input("For 1st matrix:\nEnter the RowxCol: ").split("x", 1)]
print("Enter the elements rowwise:")

for p1 in range(r1):
    a = []
    for q1 in range(c1):
         a.append(int(input()))
    s1.append(a)
print("\n1st matrix:", s1)

r2, c2 = [int(f) for f in input("For 2nd matrix:\nEnter the RowxCol: ").split("x", 1)]
print("Enter the elements rowwise:")

for p2 in range(r2):
    b = []
    for q2 in range(c2):
         b.append(int(input()))
    s2.append(b)
print("\n2nd matrix:", s2)
print()
print(matmult(s1,s2))