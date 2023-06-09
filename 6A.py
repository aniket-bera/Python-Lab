arr = []

n = int(input("Enter number of elements for 1D array: "))
print("Enter",n,"elements: ")

for i in range(n):
    e = int(input())
    arr.append(e)
    
print("\n1D array elements:", arr)

min = arr[0];
max = arr[0];

for i in range(n):
    if(arr[i] < min):
        min = arr[i];
    
    if(arr[i] > max):    
        max = arr[i];

print("\nSmallest element present in 1D array:", min)
print("Largest element present in 1D array:", max);

arr_2d = []

r = int(input("In 2D Enter the number of rows: "))
c = int(input("In 2d Enter the number of columns: "))
print("Enter the elements rowwise:")

for p in range(r):
    a = []
    for q in range(c):
         a.append(int(input()))
    arr_2d.append(a)

print("\n2D array elements:", arr_2d)

min = arr_2d[0][0]
max = arr_2d[0][0]

for i in range(r):
    for j in range(c):
        if(arr_2d[i][j] > max):
            max = arr_2d[i][j]
        
        if(arr_2d[i][j] < min):
            min = arr_2d[i][j]
        
print("\nSmallest element present in 2D array:", min)
print("Largest element present in 2D array:", max)