number = int(input())
count = 0
previous = number
biggest_jump = 0
while number != 0 :
    increase = number - previous
    count += 1
    previous = number
    if increase > biggest_jump:
        biggest_jump = increase
    number = int(input())

print(count)
print(biggest_jump)
