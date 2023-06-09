try:
    a = input("Enter 1st number: ")
    b = input("Enter 2nd number: ")
    
    if a.isdigit() and b.isdigit():
        c = eval(a) + eval(b)
        print("Sum of two number:",c)
    else:
        raise Exception
except:
    print("Something else went wrong!!")