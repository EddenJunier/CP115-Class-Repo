yardLength = float(input())
yardWidth = float(input())
houseArea = yardLength * yardWidth
houseLength = float(input())
houseWidth = float(input())
builtInHouse = houseLength * houseWidth
wage = houseArea - builtInHouse * 2
print(wage)
