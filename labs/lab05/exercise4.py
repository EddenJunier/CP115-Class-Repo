#Shopping cost calculator
itemname1 = input("Enter the name of the first item: ")
item1_price = float(input((f"Enter the price of {itemname1}: ")))
itemname2 = input("Enter the name of the second item: ")
item2_price = float(input(f"Enter the price of {itemname2}: "))
itemname3 = input("Enter the name of the third item: ")
item3_price = float(input(f"Enter the price of {itemname3}: "))

subtotal_cost = item1_price + item2_price + item3_price
tax_amount = 0.06 * subtotal_cost
total_cost = subtotal_cost + tax_amount


print(f"\nSubtotal: ${subtotal_cost:.2f}")
print(f"Tax: ${tax_amount:.2f}")
print(f"Total Cost: ${total_cost:.2f}")