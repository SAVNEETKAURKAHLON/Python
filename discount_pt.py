type = input("enter user type 'r' or 'w' for cutomer type ,if you do not have customer type leave blank ")
purchase = int(input("enetr the amount of your purchase "))

if(type == "r"):
    if( purchase> 0 and purchase < 100):
        print("discount percent is 0.1")
        total = purchase*0.1
        print("your total amount is ",total)
    elif( purchase  >= 100 and purchase < 250):
        print("discount percent is 0.2")
        total = purchase*0.2
        print("your total amount is ",total)
    elif( purchase  >= 250 and purchase < 500):
        print("discount percent is 0.3")
        total = purchase*0.3
        print("your total amount is ",total)
    else:
        print("discount percent is 0.4")
        total = purchase*0.4
        print("your total amount is ",total)
elif(type == "w"):
     if( purchase> 0 and purchase < 300):
        print("discount percent is 0.15")
        total = purchase*0.15
        print("your total amount is ",total)
     elif( purchase  >= 300 and purchase < 600):
        print("discount percent is 0.25")
        total = purchase*0.25
        print("your total amount is ",total)
     else:
        print("discount percent is 0.35")
        total = purchase*0.35
        print("your total amount is ",total)
else:
    print("no discount as no customer type or not valid customer type entered")
    print("your total amount is ",purchase)