# Salary Hike Calculator
print("Salary Hike Calculator")

#enter employee name
employee_name = input("Enter Employee Name: ")

#input monthly salary
old_salary = float(input("Enter Old Monthly Salary (INR): "))
new_salary = float(input("Enter New Monthly Salary (INR): "))

#calculate hike
hike_amount = new_salary - old_salary
hike_percentage = (hike_amount / old_salary) * 100

#display result
print("\n----- SALARY DETAILS -----")
print(f"Old Monthly Salary : {old_salary:.2f} INR")
print(f"New Monthly Salary : {new_salary:.2f} INR")

#display hike details
print("\n----- HIKE DETAILS -----")
print(f"Monthly Hike Amount : {hike_amount:.2f} INR")
print(f"Hike Percentage     : {hike_percentage:.2f}%")