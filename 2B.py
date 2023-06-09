basicP = eval(input("Enter your basic pay: "))

AGP = 0.50 * basicP

DA = (basicP + AGP) * 0.50

HRA = (basicP + AGP) * 0.15

NetS = ((basicP + AGP) + DA + HRA)

print("Total Salary =", NetS)