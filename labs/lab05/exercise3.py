#random student selector

import random

# Get the total number of items first
n = int(input("How many students do you wants to enter? (total number of students): "))
students = []

# Loop n times to collect each item
for i in range(n):
    item = input(f"Enter student {i+1}: ")
    students.append(item)


selected_student = random.choice(students)
print("\n")

print(f"Selected student: {selected_student}")
print("\n")

print("Sellected stdent will be enrolled into military training for 3 months as a punishment for not attending class on time and not submitting assignments on time. ")
print("\n")
