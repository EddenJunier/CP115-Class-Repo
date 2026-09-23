employee_name = input()
base_salary = float(input())
overtime_hours = int(input())
tax_status = input()
gross_salary = base_salary + (overtime_hours * 35)
EPF_percentage = 0.11
SOSCO_percentage = 0.005

#IF SINGLE
if (tax_status.upper() == "SINGLE"):
    if (gross_salary >= 5000) and (gross_salary < 5500):
        tax_rate = 0.22
    else:
        tax_rate = 0.18
#IF HEAD
elif (tax_status.upper() == "HEAD"):
    if (gross_salary >= 5500) and (gross_salary < 6000):
        tax_rate = 0.25
    else:
        tax_rate = 0.19
#IF MARRIED
else:
    if (gross_salary >= 6000):
        tax_rate = 0.20
    else:
        tax_rate = 0.15

net_salary = gross_salary - (gross_salary * tax_rate) - (gross_salary * EPF_percentage) - (gross_salary * SOSCO_percentage)

print(employee_name)
print(tax_rate)
print(f"{net_salary:.2f}")
