main_course = input()
drink = input()
dessert = input()

food_cost = 0.0
# Determine main course price
if main_course == "Chicken":
    food_cost += 10
elif main_course == "Beef":
    food_cost += 12
elif main_course == "Fish":
    food_cost += 11

# Determine drink price
if drink == "Soft Drink":
    food_cost += 2
elif drink == "Coffee":
    food_cost += 3

# Determine dessert price
if dessert == "Ice Cream":
    food_cost += 4
elif dessert == "Cake":
    food_cost += 5

# Calculate final bill with 10% service charge
final_bill = food_cost + (food_cost * 0.10)

# Output the final bill to two decimal places
print(f"{final_bill:.2f}")
