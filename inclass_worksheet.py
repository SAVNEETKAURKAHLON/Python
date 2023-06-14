cap_yes = "Yes"
small_yes = "yes"
cap_no ="No"
small_no = "no"
print(cap_yes < small_yes)
print(cap_no < small_no)
print(cap_yes > small_yes)
print(cap_no > small_no)


day = input("please enter the day of your visit")
ticket_price = 50
status = input("please enter your status")

print( "the price of the ticket is 50:",day == "weekday" and status == "student") 