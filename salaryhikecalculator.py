import matplotlib.pyplot as plt

# Salary Hike Calculator

old_salary = float(input("Enter old monthly salary: ₹"))
new_salary = float(input("Enter new monthly salary: ₹"))

if old_salary <= 0:

    print("Old salary must be greater than 0.")

else:

    # Yearly salary
    old_yearly = old_salary * 12
    new_yearly = new_salary * 12

    # Hike amount
    hike_amount = new_salary - old_salary

    # Hike percentage
    hike_percentage = (hike_amount / old_salary) * 100

    # Display result
    print("\n----- SALARY HIKE -----")
    print(f"Old Monthly Salary : ₹{old_salary:.2f}")
    print(f"New Monthly Salary : ₹{new_salary:.2f}")
    print(f"Monthly Hike       : ₹{hike_amount:.2f}")
    print(f"Hike Percentage    : {hike_percentage:.2f}%")


    print("\n----- YEARLY SALARY -----")
    print(f"Old Yearly Salary  : ₹{old_yearly:.2f}")
    print(f"New Yearly Salary  : ₹{new_yearly:.2f}")
    print(f"Yearly Hike        : ₹{new_yearly - old_yearly:.2f}")

    # BAR CHART

    salary = [old_salary, new_salary]

    salary_type = [
        "Old Salary",
        "New Salary"
    ]

    # Create bar chart
    plt.bar(salary_type, salary)

    # Title
    plt.title("Salary Hike Comparison")

    # X-axis
    plt.xlabel("Salary Type")

    # Y-axis
    plt.ylabel("Monthly Salary (₹)")

    # Show values
    for i, value in enumerate(salary):

        plt.text(
            i,
            value,
            f"₹{value:.0f}",
            ha="center",
            va="bottom"
        )
    # Display chart
    plt.show()