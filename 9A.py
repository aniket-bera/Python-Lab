import calculator
while True:
    x = eval(input("Enter 1st number: "))
    c = input("Enter your operator [+, -, *, /, ^, %]: ")
    y = eval(input("Enter 2nd number: "))
    if c in ('+', '-', '*', '/', '^', '%'):
        if c == '+':
            print("\n{} {} {} = {}".format(x,c,y,calculator.add(x, y)))
        elif c == '-':
            print("\n{} {} {} = {}".format(x,c,y,calculator.subtraction(x, y)))
        elif c == '*':
            print("\n{} {} {} = {}".format(x,c,y,calculator.multiply(x, y)))
        elif c == '/':
            print("\n{} {} {} = {}".format(x,c,y,calculator.divide(x, y)))
        elif c == '^':
            print("\n{} {} {} = {}".format(x,c,y,calculator.exponent(x, y)))
        elif c == '%':
            print("\nResult = {}%".format(calculator.percentage(x, y)))
        next_op = input("Another operation? [y/n] --> ")
        if next_op != 'y' or next_op == 'n':
            print("---Quit---")
            break
    else:
        print("Invalid Input!!!")