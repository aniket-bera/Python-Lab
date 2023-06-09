n = int(input())

def sumofsquares(n):
    if n < 0:
        return False
    for i in range(1, int(n**0.5)  + 1 ):
        for j in range(1, int(n**0.5) + 1 ):
            m = i**2 + j**2
            if m == n:
                return True
            elif m > n:
                break
    return False

print(sumofsquares(n))