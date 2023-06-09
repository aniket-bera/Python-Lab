def fact(num):
    f = 1
    for i in range(1, num + 1):
        f = f * i
    return f

def special(temp):
    data = temp
    sum = 0
    while temp != 0:
        rem = temp % 10
        temp = temp // 10
        sum = sum + fact(rem)
    if data == sum:
        return True
    else:
        return False
    
start, end = [int(p) for p in input("Enter range of checking numbers: ").split("-", 1)]

for p in range(start, end + 1):
    if special(p):
        print(p)