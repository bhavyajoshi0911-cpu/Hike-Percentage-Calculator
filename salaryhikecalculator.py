# Salary Hike Calculator

# This program calculates the salary hike based on the old and new monthly salaries provided by the user.
old_salary = float(input("Enter old monthly salary: "))
new_salary = float(input("Enter new monthly salary: "))

# Calculate yearly salaries and hike details
old_yearly = old_salary * 12
new_yearly = new_salary * 12

# Calculate hike amount and percentage
hike_amount = new_salary - old_salary
hike_percentage = (hike_amount / old_salary) * 100

# Display the results monthly and yearly
print("\n----- SALARY HIKE -----")
print(f"Old Monthly Salary : ₹{old_salary:.2f}")
print(f"New Monthly Salary : ₹{new_salary:.2f}")
print(f"Monthly Hike       : ₹{hike_amount:.2f}")
print(f"Hike Percentage    : {hike_percentage:.2f}%")

print("\n----- YEARLY SALARY -----")
print(f"Old Yearly Salary  : ₹{old_yearly:.2f}")
print(f"New Yearly Salary  : ₹{new_yearly:.2f}")
print(f"Yearly Hike        : ₹{new_yearly - old_yearly:.2f}")