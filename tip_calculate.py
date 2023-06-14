meal_cost = 52.31
tip_percent = 20

tip = meal_cost*(tip_percent/100)
total_amount = meal_cost + tip
print("Tip Calculator")
print("cost of meal:",meal_cost)
print("Tip Percent:",tip_percent)
print()
print("Tip Amount:",round(tip,2))
print("Total Amount:",round(total_amount,2))
