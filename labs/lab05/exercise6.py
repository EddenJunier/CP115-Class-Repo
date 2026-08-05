#time converter

time_in_minutes = int(input("Enter time in minutes: "))
hours = time_in_minutes // 60
minutes = time_in_minutes % 60

print(f"\nTime in minutes: {time_in_minutes}")
print(f"time in hours: {hours}")
print(f"{time_in_minutes} minutes is equal to {hours} hours and {minutes} minutes.")