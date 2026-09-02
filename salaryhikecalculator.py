# ============================================================
#             SALARY HIKE PERCENTAGE CALCULATOR
# ============================================================

import os
import json
from datetime import datetime
import statistics
import matplotlib.pyplot as plt


HISTORY_FILE = "salary_history.json"


# ------------------------------------------------------------
# 1. INPUT VALIDATION
# ------------------------------------------------------------

def get_positive_salary(message):
    """Take a valid positive salary from the user."""

    while True:
        try:
            salary = float(input(message))

            if salary <= 0:
                print("❌ Salary must be greater than 0.")
            else:
                return salary

        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")


# ------------------------------------------------------------
# 2. CALCULATE HIKE
# ------------------------------------------------------------

def calculate_hike(old_salary, new_salary):
    """Calculate hike amount and percentage."""

    hike_amount = new_salary - old_salary
    hike_percentage = (hike_amount / old_salary) * 100

    return hike_amount, hike_percentage


# ------------------------------------------------------------
# 3. YEARLY SALARY
# ------------------------------------------------------------

def calculate_yearly_salary(monthly_salary):
    """Convert monthly salary into yearly salary."""

    return monthly_salary * 12


# ------------------------------------------------------------
# 4. HIKE STATUS
# ------------------------------------------------------------

def get_hike_status(hike_percentage):

    if hike_percentage > 0:
        return "🎉 Salary Increased"

    elif hike_percentage == 0:
        return "ℹ️ No Salary Change"

    else:
        return "⚠️ Salary Decreased"


# ------------------------------------------------------------
# 5. HIKE CATEGORY
# ------------------------------------------------------------

def get_hike_category(hike_percentage):

    if hike_percentage >= 30:
        return "Excellent Hike 🚀"

    elif hike_percentage >= 20:
        return "Very Good Hike 👍"

    elif hike_percentage >= 10:
        return "Good Hike 🙂"

    elif hike_percentage > 0:
        return "Small Hike"

    elif hike_percentage == 0:
        return "No Hike"

    else:
        return "Salary Decrease"


# ------------------------------------------------------------
# 6. SAVE HISTORY USING JSON
# ------------------------------------------------------------

def save_history(data):

    history = []

    if os.path.exists(HISTORY_FILE):

        try:
            with open(HISTORY_FILE, "r") as file:
                history = json.load(file)

        except json.JSONDecodeError:
            history = []

    history.append(data)

    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=4)

    print("\n✅ Salary calculation saved successfully!")


# ------------------------------------------------------------
# 7. SHOW HISTORY
# ------------------------------------------------------------

def show_history():

    if not os.path.exists(HISTORY_FILE):

        print("\n❌ No salary history found.")
        return

    with open(HISTORY_FILE, "r") as file:
        history = json.load(file)

    if not history:

        print("\n❌ No salary history available.")
        return

    print("\n" + "=" * 70)
    print("                  SALARY HISTORY")
    print("=" * 70)

    for index, record in enumerate(history, start=1):

        print(f"\nRecord #{index}")
        print(f"Employee       : {record['employee_name']}")
        print(f"Old Salary     : ₹{record['old_salary']:,.2f}")
        print(f"New Salary     : ₹{record['new_salary']:,.2f}")
        print(f"Hike Amount    : ₹{record['hike_amount']:,.2f}")
        print(f"Hike Percentage: {record['hike_percentage']:.2f}%")
        print(f"Date           : {record['date']}")


# ------------------------------------------------------------
# 8. STATISTICS
# ------------------------------------------------------------

def show_statistics():

    if not os.path.exists(HISTORY_FILE):

        print("\n❌ No data available.")
        return

    with open(HISTORY_FILE, "r") as file:
        history = json.load(file)

    if not history:

        print("\n❌ No data available.")
        return

    percentages = [
        record["hike_percentage"]
        for record in history
    ]

    average_hike = statistics.mean(percentages)
    maximum_hike = max(percentages)
    minimum_hike = min(percentages)

    print("\n" + "=" * 50)
    print("             HIKE STATISTICS")
    print("=" * 50)

    print(f"Average Hike : {average_hike:.2f}%")
    print(f"Highest Hike : {maximum_hike:.2f}%")
    print(f"Lowest Hike  : {minimum_hike:.2f}%")

    print("=" * 50)


# ------------------------------------------------------------
# 9. CREATE CHART
# ------------------------------------------------------------

def show_chart(old_salary, new_salary):

    salaries = [
        old_salary,
        new_salary
    ]

    labels = [
        "Old Salary",
        "New Salary"
    ]

    plt.figure(figsize=(8, 5))

    plt.bar(labels, salaries)

    plt.title("Salary Comparison")

    plt.ylabel("Monthly Salary (₹)")

    plt.tight_layout()

    plt.show()


# ------------------------------------------------------------
# 10. DISPLAY RESULT
# ------------------------------------------------------------

def display_result(
    employee_name,
    old_salary,
    new_salary,
    hike_amount,
    hike_percentage
):

    old_yearly = calculate_yearly_salary(old_salary)

    new_yearly = calculate_yearly_salary(new_salary)

    yearly_hike = new_yearly - old_yearly

    print("\n" + "=" * 60)
    print("               SALARY HIKE REPORT")
    print("=" * 60)

    print(f"Employee Name     : {employee_name}")

    print("\n----- MONTHLY SALARY -----")

    print(f"Old Salary        : ₹{old_salary:,.2f}")

    print(f"New Salary        : ₹{new_salary:,.2f}")

    print(f"Hike Amount       : ₹{hike_amount:,.2f}")

    print(f"Hike Percentage   : {hike_percentage:.2f}%")

    print("\n----- YEARLY SALARY -----")

    print(f"Old Yearly Salary : ₹{old_yearly:,.2f}")

    print(f"New Yearly Salary : ₹{new_yearly:,.2f}")

    print(f"Yearly Hike       : ₹{yearly_hike:,.2f}")

    print("\n----- ANALYSIS -----")

    print(f"Status            : {get_hike_status(hike_percentage)}")

    print(f"Category          : {get_hike_category(hike_percentage)}")

    print("=" * 60)


# ------------------------------------------------------------
# 11. MAIN PROGRAM
# ------------------------------------------------------------

def main():

    print("\n" + "=" * 60)
    print("          💼 SALARY HIKE CALCULATOR")
    print("=" * 60)

    while True:

        print("\n1. Calculate Salary Hike")
        print("2. View Salary History")
        print("3. View Hike Statistics")
        print("4. Exit")

        choice = input("\nEnter your choice: ").strip()

        # ----------------------------------------------------
        # CALCULATOR
        # ----------------------------------------------------

        if choice == "1":

            employee_name = input(
                "\nEnter Employee Name: "
            ).strip()

            if not employee_name:

                print("❌ Employee name cannot be empty.")

                continue

            old_salary = get_positive_salary(
                "Enter Old Monthly Salary: ₹"
            )

            new_salary = get_positive_salary(
                "Enter New Monthly Salary: ₹"
            )

            hike_amount, hike_percentage = calculate_hike(
                old_salary,
                new_salary
            )

            display_result(
                employee_name,
                old_salary,
                new_salary,
                hike_amount,
                hike_percentage
            )

            # Create record
            record = {

                "employee_name": employee_name,

                "old_salary": old_salary,

                "new_salary": new_salary,

                "hike_amount": hike_amount,

                "hike_percentage": hike_percentage,

                "date": datetime.now().strftime(
                    "%d-%m-%Y %H:%M:%S"
                )
            }

            save_history(record)

            # Chart
            show_chart(
                old_salary,
                new_salary
            )

        # ----------------------------------------------------
        # HISTORY
        # ----------------------------------------------------

        elif choice == "2":

            show_history()

        # ----------------------------------------------------
        # STATISTICS
        # ----------------------------------------------------

        elif choice == "3":

            show_statistics()

        # ----------------------------------------------------
        # EXIT
        # ----------------------------------------------------

        elif choice == "4":

            print("\nThank you for using Salary Hike Calculator! Goodbye!")

            break

        else:

            print("\n❌ Invalid choice. Please select 1-4.")

# ------------------------------------------------------------
# PROGRAM START
# ------------------------------------------------------------

if __name__ == "__main__":

    main()