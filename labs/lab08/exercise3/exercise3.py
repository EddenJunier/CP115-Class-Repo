day_type = input()
show_time = int(input())
customer_type = input()
base_price = 0

#weekday price
if day_type.upper() == "WEEKEND":
    if customer_type.upper() == "ADULT":
        base_price = 18
    elif customer_type.upper() == "CHILD":
        base_price = 12
    else:
        base_price = 15

#weekend price
if day_type.upper() == "WEEKDAY":
    if customer_type.upper() == "ADULT":
        base_price = 15
    elif customer_type.upper() == "CHILD":
        base_price = 10
    else:
        base_price = 12

#time for final price
if show_time > 18 :
    final_price = base_price + 3
else:
    final_price = base_price

print(base_price)
print(final_price)
