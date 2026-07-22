weight = float(input())
if weight <= 5:
    totalCharge = weight * 8
else:
    first5Kg = 5 * 8
    additionalKg = weight - 5
    additionalCharge = additionalKg * 6
    totalCharge = first5Kg + additionalCharge
if totalCharge > 60:10
    totalCharge = totalCharge + 10
print(weight)
print(totalCharge)
