# Salary Hike Calculator
print("Salary Hike Calculator")

#enter employee name
employee_name = input("Enter Employee Name: ")

# Take salary input
old_salary = float(input("Enter your old monthly salary: "))
new_salary = float(input("Enter your new monthly salary: "))

# Calculate hike amount
hike_amount = new_salary - old_salary

# Calculate hike percentage
hike_percentage = (hike_amount / old_salary) * 100

# Calculate yearly salary
old_yearly_salary = old_salary * 12
new_yearly_salary = new_salary * 12

# Calculate yearly hike
yearly_hike = new_yearly_salary - old_yearly_salary

# Display result
print("\n----- Salary Details -----")

print(f"Old Monthly Salary  : ₹{old_salary:.2f}")
print(f"New Monthly Salary  : ₹{new_salary:.2f}")
print(f"Monthly Hike Amount  : ₹{hike_amount:.2f}")
print(f"Hike Percentage     : {hike_percentage:.2f}%")

print("\n----- Yearly Salary -----")

print(f"Old Yearly Salary   : ₹{old_yearly_salary:.2f}")
print(f"New Yearly Salary   : ₹{new_yearly_salary:.2f}")
print(f"Yearly Hike Amount  : ₹{yearly_hike:.2f}")

# Hike status
if hike_percentage > 0:
    print("\nCongratulations! You got a salary hike.")
elif hike_percentage == 0:
    print("\nYour salary has not changed.")
else:
    print("\nYour salary has decreased.")