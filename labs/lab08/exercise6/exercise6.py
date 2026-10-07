position = input()
overtime_hours = int(input())
is_weekend = input()

# 1. Determine base hourly rate
base_rate = 0.0
if position == "Manager":
    base_rate = 30.0
elif position == "Supervisor":
    base_rate = 20.0
elif position == "Staff":
    base_rate = 15.0
elif position == "Intern":
    base_rate = 8.0

# 2. Calculate progressive overtime pay
overtime_pay = 0.0
if overtime_hours <= 8:
    overtime_pay = overtime_hours * (base_rate * 1.5)
else:
    overtime_pay = (8 * (base_rate * 1.5)) + ((overtime_hours - 8) * (base_rate * 2.0))

# 3. Add weekend bonus if applicable
if is_weekend == "yes":
    overtime_pay += overtime_hours * 5.0


print(overtime_pay)
