cost = float(input("enter the total purchase "))
if(cost > 0):
    if( cost  < 30):
        print("Shipping cost is 5.95")
    elif( cost >=30 and cost <= 49.99):
        print("Shipping cost is 7.95")
    elif( cost >= 50 and cost <= 74.99):
        print("Shipping cost is 9.95")
    else:
        print("Wohoo! no shipping cost")
else:
    print("ERROR!please enter a valid number")


cost = int(input("enter the cost of your meal"))
if( cost > 0):
    print("On tip of 15% , tip amount is ",(cost*0.15))
    total = cost  + (cost*0.15)
    print("total cost is ",total)

    print("On tip of 20% , tip amount is ",(cost*0.20))
    total = cost  + (cost*0.20)
    print("total cost is ",total)

    print("On tip of 25% , tip amount is ",(cost*0.25))
    total = cost  + (cost*0.25)
    print("total cost is ",total)

else:
    print("enetr valid value")