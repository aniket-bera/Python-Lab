import numpy as np

while True:  
    print("\nSelect your searching technique:")  
    print("1 --> Linear Search")  
    print("2 --> Binary Search")  
    print("3 --> Exit")
    choice = int(input("Enter the Choice: "))
    
    if choice == 1:
        n = int(input("Enter number of elements: "))
        arr = np.empty(n, dtype = int)
        print("Enter {} elements:".format(n))

        for i in range(n):
            arr[i] = int(input())

        print("\nInitial array elements are:", arr)
              
        s = int(input("Enter the element to search: "))
        
        count = 0
        
        for i in range(n):
            if arr[i] == s:
                print("{} is present at location {}".format(s, i+1))
                count += 1

        if count == 0:
            print("{} is not present in array.".format(s))
        else:
            print("{} is present {} times in array.".format(s, count))
    
    elif choice == 2:
        n = int(input("Enter number of elements: "))
        arr = np.empty(n, dtype = int)
        print("Enter {} elements is ascending order:".format(n))

        for i in range(n):
            arr[i] = int(input())

        print("\nInitial sorted array is:", arr)
        
        s = int(input("Enter the element to search: "))
        
        first = 0
        last = n - 1
        mid = (first + last) // 2
        
        while first <= last:
            if arr[mid] < s:
                first = mid + 1
        
            elif arr[mid] == s:
                print("{} found at location {}".format(s, mid+1))
                break

            else:
                last = mid - 1
            
            mid = (first + last) // 2

            if first > last:
                print("{} is not present in array.".format(s))        

    elif choice == 3:
        break
    
    else:
        print("Invalid choice!!!")