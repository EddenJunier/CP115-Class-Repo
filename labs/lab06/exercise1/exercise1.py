# Escape Characters Exercise
# Print the receipt shown in the lab, using \n for new lines and \t for columns.
# Calculate every total, subtotal, and tax in your code. Do not type the money
# amounts in directly. Show every amount with exactly two decimal places.

Coffee_price = 3.50
Muffin_price = 2.10
Water_price = 1.05
Coffee_qty = 2
Muffin_qty = 3
Water_qty = 4

Coffee_total = Coffee_price * Coffee_qty
Muffin_total = Muffin_price * Muffin_qty
Water_total = Water_price * Water_qty

Subtotal = Coffee_total + Muffin_total + Water_total

tax = (Subtotal/100) * 6
total = Subtotal + tax

#Print for each line
print("========== RECEIPT ==========")
print("Item\tPrice\tQty\tTotal")
print(f"Coffee\t${Coffee_price:.2f}\t{Coffee_qty}\t{Coffee_total:.2f}")
print(f"Muffin\t${Muffin_price:.2f}\t{Muffin_qty}\t{Muffin_total:.2f}")
print(f"Water\t${Water_price:.2f}\t{Water_qty}\t{Water_total:.2f}")
print("------------------------------")
print(f"Subtotal\t\t{Subtotal:.2f}")
print(f"Tax (6%)\t\t{tax:.2f}")
print(F"Total\t\t\t{total:.2f}")
print("============================")

print("\n")
print("\n")

#only 1 print for every line
#Much simple because not need to type print for each line

print(f"""
========== RECEIPT ==========
Item\tPrice\tQty\tTotal
Coffee\t${Coffee_price:.2f}\t{Coffee_qty}\t{Coffee_total:.2f}
Muffin\t${Muffin_price:.2f}\t{Muffin_qty}\t{Muffin_total:.2f}
Water\t${Water_price:.2f}\t{Water_qty}\t{Water_total:.2f}
------------------------------
Subtotal\t\t{Subtotal:.2f}
Tax (6%)\t\t{tax:.2f}
Total\t\t\t{total:.2f}
============================
""")