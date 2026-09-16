# Get employee information
employee_name = input("Enter employee name: ")
hourly_rate = float(input("Enter hourly rate: "))
while hourly_rate <= 0:
    print("Error: Hourly rate cannot be negative.")
    hourly_rate = float(input("Enter hourly rate: "))
hours_worked = float(input("Enter hours worked: "))
while hours_worked <= 0:
    print("Error: Hours worked cannot be negative.")
    hours_worked = float(input("Enter hours worked: "))
if hours_worked > 80:
    overtime_hours = hours_worked - 80
    regular_hours = 80
else:
    overtime_hours = 0
    regular_hours = hours_worked
print("Regular hours worked:", regular_hours)
print("Overtime hours worked:", overtime_hours)
# Determine regular and overtime hours
regular_pay = regular_hours * hourly_rate
overtime_rate = hourly_rate * 1.5
overtime_pay = overtime_hours * overtime_rate
# Calculate pay and deductions
gross_pay = regular_pay + overtime_pay
tax_rate = float(input("Enter tax rate percentage: ")) / 100
while tax_rate < 0 or tax_rate > 100:
    print("Error: Tax rate must be between 0 and 100.")
    tax_rate = float(input("Enter tax rate percentage: ")) / 100
tax_amount = gross_pay * tax_rate
retirement_rate = float(input("Enter retirement rate percentage: ")) / 100
while retirement_rate < 0 or retirement_rate > 100:
    print("Error: Retirement rate must be between 0 and 100.")
    retirement_rate = float(input("Enter retirement rate percentage: ")) / 100
retirement_amount = gross_pay * retirement_rate
net_pay = gross_pay - tax_amount - retirement_amount
# Display payroll summary
print("\n------ PAYROLL SUMMARY ------")
print(f"Employee: {employee_name}")
print(f"Hourly Rate: ${hourly_rate:,.2f}")
print(f"Regular Hours: {regular_hours}")
print(f"Overtime Hours: {overtime_hours}")
print(f"Regular pay: ${regular_pay:,.2f}")
print(f"Overtime pay: ${overtime_pay:,.2f}")
print(f"Gross pay: ${gross_pay:,.2f}")
print(f"Tax Deduction: ${tax_amount:,.2f}")
print(f"Retirement Contribution: ${retirement_amount:,.2f}")
print(f"Net Pay: ${net_pay:,.2f}")