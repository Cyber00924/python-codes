year=int(input("enter the number: "))
if((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
    print("it is a leap year")
else:
    print("it is not a leap year")
