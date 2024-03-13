annual_salary = float(input("Enter the starting salary: "))

total_cost = 1000000
semi_annual_raise = 0.07
portion_down_payment = 0.25
down_payment = total_cost * portion_down_payment
R = 0.04

portion_saved_rates = range(0, 10000)
month_count_expect = 36
bisection = 0
last_portion_saved = False

high = len(portion_saved_rates) - 1
low = 0
found = False

while low <= high:
    bisection += 1
    mid = (high + low) // 2
    portion_saved = portion_saved_rates[mid] / 10000.0
    current_savings = 0
    current_annual_salary = annual_salary
    month_count = 0

    while month_count < month_count_expect:
        current_savings += current_savings * R / 12 + current_annual_salary / 12 * portion_saved
        month_count += 1
        if month_count % 6 == 0:
            current_annual_salary += current_annual_salary * semi_annual_raise

    if abs(current_savings - down_payment) <= 100:
        last_portion_saved = portion_saved_rates[mid]
        found = True
        break
    elif current_savings < down_payment:
        low = mid + 1
    else:
        high = mid - 1

if found:
    print("Best savings rate: {:.4f}".format(last_portion_saved / 10000))
    print("Steps in bisection search: {}".format(bisection))
else:
    print("It is not possible to pay the down payment in three years.")
