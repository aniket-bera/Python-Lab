n = int(input("Number of classes held: "))
a = int(input("Number of classes attended: "))

p = (a / n) * 100
print("Percentage of attendance is %.1f " %p)

if p < 75:
    print("\nDid he/she has any medical cause?")
    print("If Yes then press --> Y\nIf No then press --> N")
    issue = input("[Y/N] --> ")
    
    if issue == "Y":
        print("He/She is allowed to sit in the exam.")
    
    elif issue == "N":
        print("He/She is not allowed to sit in the exam.")
    
    else:
        print("Invalid input!!!")