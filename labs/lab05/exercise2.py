import math
import random

radius = float(input("Enter the radius of the circle: "))

circle_area = math.pi *(radius ** 2)
circle_circumference = 2 * math.pi * radius

print(f"\nCircle Area: {circle_area:.2f}")
print(f"Circle Circumference: {circle_circumference:.2f}")