num_days = int(input())
danger_threshold = float(input())
danger_days = 0

total_temperature = 0

for i in range (num_days):
    temperature = float(input())
    if temperature > danger_threshold :
        danger_days += 1
        total_temperature += temperature
    else:
        total_temperature += temperature

running_total = num_days
average_temp = (total_temperature / running_total)
print(danger_days)
print(f"{average_temp:.1f}")
