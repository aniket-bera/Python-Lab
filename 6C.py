import numpy as np

n = int(input("Enter number of elements: "))
arr = np.empty(n, dtype = int)
print("Enter",n,"elements:")

for i in range(n):
    arr[i] = int(input())

print("\nInitial array elements are: ", arr)
    
while True:  
    print("\nSelect your sorting technique:")  
    print("1 --> Bubble Sort")  
    print("2 --> Selection sort")  
    print("3 --> Insertion Sort")
    print("4 --> Exit")
    choice = int(input("Enter the Choice: "))
    
    if choice == 1:
        for i in range(n -1):
            for j in range(n - i - 1):
                if(arr[j] > arr[j + 1]):
                     temp = arr[j]
                     arr[j] = arr[j + 1]
                     arr[j + 1] = temp

        print("Bubble Sort:\nSorted elements are:", arr)
    
    elif choice == 2:
        for i in range(n):
            p_min = i
    
            for j in range(i+1, n):
              if (arr[j] < arr[p_min]):
                minimum = j
        
            temp = arr[i]
            arr[i] = arr[p_min]
            arr[p_min] = temp

        print("Selection Sort:\nSorted elements are:", arr)
    
    elif choice == 3:
        for i in range(1, n):
            temp = arr[i]
            j = i - 1

            while j >= 0 and temp < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
    
            arr[j + 1] = temp
        
        print("Insertion Sort:\nSorted elements are:", arr)
    
    elif choice == 4:
        break
    
    else:
        print("Invalid choice!!!")