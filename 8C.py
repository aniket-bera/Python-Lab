'''n = int(input("No. of elements: "))
data = []

for i in range(n):
    item = input()
    data.append(item)

rotate = int(input("No. of rotation: "))
   
for i in range(0, rotate):
    p = data[len(data) - 1]
    
    for j in range(len(data)-1, -1):    #start,stop,step
        data[j] = data[j - 1]
    
    data[0] = p
     
for i in range(0, len(data)):
    print(data[i], end = " ")'''
    
def rlist(p, k):
    if(k < 0):
        return p
    s = len(p)
    k = k % s
    q = p[s - k:] + p[:s - k]
    return q

n = int(input("No. elements: "))

p = []

for i in range(n):
    a = int(input())
    p.append(a)

r = int(input("No. of rotation: "))
print(rlist(p, r))