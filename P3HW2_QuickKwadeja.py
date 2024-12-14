# Kwadeja Quick
# October 26th, 2024
# Decision Structures 
def calculate_pay():
    # Ask for employee details
    employee_name = input("Enter the name of the employee: ")
    hours_worked = float(input("Enter number of hours worked this week: "))
    pay_rate = float(input("Enter employee's pay rate: "))

    # Constants
    overtime_threshold = 40
    overtime_rate = 1.5

    # Calculate regular and overtime hours
    if hours_worked > overtime_threshold:
        regular_hours = overtime_threshold
        overtime_hours = hours_worked - overtime_threshold
    else:
        regular_hours = hours_worked
        overtime_hours = 0

    # Calculate pay
    regular_pay = regular_hours * pay_rate
    overtime_pay = overtime_hours * pay_rate * overtime_rate
    gross_pay = regular_pay + overtime_pay

    # Display the results
    print("\nEmployee Pay Details:")
    print(f"Employee Name: {employee_name}")
    print(f"Pay Rate: ${pay_rate:.2f} per hour")
    print(f"Number of Hours Worked: {hours_worked:.2f} hours")
    print(f"Overtime Hours: {overtime_hours:.2f} hours")
    print(f"Overtime Pay: ${overtime_pay:.2f}")
    print(f"Pay for Regular Hours: ${regular_pay:.2f}")
    print(f"Gross Pay: ${gross_pay:.2f}")

# Run the program
calculate_pay()
