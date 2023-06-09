cu = eval(input("Consumption Unit: "))

if cu >= 0 and cu <= 200:
    t = cu * 0.50

elif cu >= 201 and cu <= 400:
    t = (cu * 0.65) + 100

elif cu >= 401 and cu <= 600:
    t = (cu * 0.80) + 200

elif cu > 600:
    t = (cu * 1.00) + 300

else:
    print("Invalid input!!!")

print("Your total paid amount: %.2f" %t)