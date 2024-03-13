annual_salary = float(input("Enter your starting annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semiannual raise, as a decimal: "))

portion_down_payment = 0.25 * total_cost
r = 0.04

current_savings = 0.0
months = 0

while current_savings < portion_down_payment:
    current_savings += current_savings * (r / 12)

    current_savings += (annual_salary / 12) * portion_saved

    months += 1

    if months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise

print("Number of months:", months)
