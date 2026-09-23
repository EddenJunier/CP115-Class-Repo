current_reading = int(input())
previous_reading = int(input())
consumption = current_reading - previous_reading
service_charge = 8
sewerage = 2
if consumption <= 20:
    water_cost = consumption * 0.57
elif consumption <= 35:
    water_cost = (consumption-20) * 1.03
else:
    water_cost = consumption * 1.40

total_bill = water_cost + service_charge + sewerage

print(consumption)
print(water_cost)
print(total_bill)
