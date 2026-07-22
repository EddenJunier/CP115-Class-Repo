weight = float(input())
if weight <= 5:
    totalCharge = weight * 8
else:
    totalCharge = weight - 5 * 6 + 5 * 8
if totalCharge > 60:
    totalCharge = totalCharge + 10
print(weight)
print(totalCharge)
