#SHC

# Input yearly salary
old_salary = float(input("Enter Old Yearly Salary (LPA): "))
new_salary = float(input("Enter New Yearly Salary (LPA): "))

# Calculate hike
hike_amount = new_salary - old_salary
hike_percentage = (hike_amount / old_salary) * 100

# Display result
print("\n----- SALARY DETAILS -----")

print(f"Old Yearly Salary : {old_salary:.2f} LPA")
print(f"New Yearly Salary : {new_salary:.2f} LPA")

# Display hike details
print("\n----- HIKE DETAILS -----")

print(f"Yearly Hike Amount : {hike_amount:.2f} LPA")
print(f"Hike Percentage    : {hike_percentage:.2f}%")