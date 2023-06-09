def pattern1(r,c):
    for i in range(0,r):
        for j in range(0,c):
            if (i==0 or j==0 or i==4 or j==4) or (i==j) or (i+j)==(r-1):
                if (i==j) or (i+j)==4:
                    print(" $ ",end="")
                else:
                    print(" * ",end="")
            else:
                print("   ",end="")
        print()
        
def pattern2(r):
    for i in range(r):
        for j in range(ord('A'),ord('A')+(2*r)-1):
            if j >= (ord('A')+r-1)+i:
                print(chr((ord('A')+r-1)-(j%(ord('A')+r-1))), end = "")
            elif j <= (ord('A')+r-1)-i:
                print(chr(j), end = "")
            else:
                print(end = " ")
        print("\n", end = "")

def pattern3(r):
    for i in range(0,r):
        for j in range(0,r):
            print(" ", end = "")
            if (i + j) >= (r - 1):
                print(i+j-r+2 ,end="")
            else:
                print(" ", end = "")
        print()
        
row = int(input("Enter number of row: "))
col = int(input("Enter number of column: "))
print("1 --> Pattern1")
print("2 --> Pattern2")
print("3 --> Pattern3")
print("4 --> Exit")

while True:
    ch = int(input("Enter your choice: "))
    if ch == 1:
        pattern1(row,col)
    elif ch == 2:
        pattern2(row)
    elif ch == 3:
        pattern3(row)
    elif ch == 4:
        break
    else:
        print("Invalid input!!!")