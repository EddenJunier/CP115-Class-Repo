speed = int(input())
total_readings = 0
longest_streak = 0
calm = 0

while speed > 0 :
    total_readings += 1
   
    if speed < 20 :
        calm += 1
    else :
        calm = 0   
        
    if calm > longest_streak:
        longest_streak = calm

    speed = int(input())

print(total_readings)
print(longest_streak)
