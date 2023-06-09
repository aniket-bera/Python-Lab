import datetime as dt
def date_validation(day, month, year):
    isValidDate = True
    try:
        dt.datetime(int(year), int(month), int(day))
    except ValueError:
        isValidDate = False
    
    if(isValidDate):
        print("Yes. It's a valid date.")
    else:
        print("No. It's a invalid date.")

d = input("Enter a date d/m/y format: ")
date = d.split('/', 2)
day = date[0]
month = date[1]
year = date[2]

date_validation(day, month, year)