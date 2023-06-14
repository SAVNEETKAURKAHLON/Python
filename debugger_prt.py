print("The miles per gallon program")
print()

miles_driven = float(input("enter miles driven:    "))
gallons_used = int(input("enter gallons of gas used:  "))

if(miles_driven <= 0):
    print("miles driven must be greater than zero.Please try again")
elif(gallons_used <= 0):
    print("gallons used must be greater than xero.Please try again")
else:
    mpg = round(miles_driven / gallons_used, 2)
    print("Miles per gallon:  ",mpg)