# Kwadeja Quick
# November 10, 2024
# P4HW2
# Assignment assess student ability to edit and enhance exiting programs
"""
Pseudocode / Algorithm for Employee Pay Calculation Program:

1. Initialize variables:
   - total_overtime_pay = 0
   - total_regular_pay = 0
   - total_gross_pay = 0
   - employee_count = 0

2. Start an infinite loop to repeatedly ask for employee data until the user inputs "Done".

3. Prompt the user to input an employee's name:
   - If the name entered is "Done", terminate the loop and proceed to step 7.

4. Prompt the user to input the number of hours worked by the employee:
   - If input is invalid (non-numeric), display an error message and prompt the user again.

5. Prompt the user to input the employee's pay rate:
   - If input is invalid (non-numeric), display an error message and prompt the user again.

6. Calculate pay based on the following:
   - If hours worked > 40:
     - Regular hours = 40
     - Overtime hours = hours worked - 40
     - Regular pay = regular hours * pay rate
     - Overtime pay = overtime hours * (pay rate * 1.5)
     - Gross pay = regular pay + overtime pay
   - If hours worked <= 40:
     - Regular hours = hours worked
     - Overtime hours = 0
     - Regular pay = regular hours * pay rate
     - Overtime pay = 0
     - Gross pay = regular pay

7. Accumulate the pay totals:
   - Add regular pay to total_regular_pay
   - Add overtime pay to total_overtime_pay
   - Add gross pay to total_gross_pay
   - Increment employee_count by 1

8. Print the breakdown of the employee's pay in a horizontal format:
   - Print column headers (Employee Name, Pay Rate, Hours Worked, Regular Hours, Overtime Hours, Overtime Pay, Regular Pay, Gross Pay)
   - Print the corresponding values for the current employee in the appropriate columns.
9. After the loop ends, print the final summary:
    - Print the total number of employees entered.
    - Print the total overtime pay.
    - Print the total regular pay.
    - Print the total gross pay.

10. End the program.

"""
def calculate_pay(hours_worked, pay_rate):
    """Calculate regular pay, overtime pay, and gross pay."""
    overtime_hours = 0
    overtime_pay = 0
    regular_pay = 0
    
    # Check if there is overtime
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (pay_rate * 1.5)  # Overtime pay is 1.5x the regular rate
        regular_pay = 40 * pay_rate  # Regular pay for 40 hours
    else:
        regular_pay = hours_worked * pay_rate  # No overtime, pay for regular hours only
    
    gross_pay = regular_pay + overtime_pay
    return regular_pay, overtime_hours, overtime_pay, gross_pay


def main():
    total_overtime_pay = 0
    total_regular_pay = 0
    total_gross_pay = 0
    num_employees = 0
    
    while True:
        # Ask for employee's name
        employee_name = input("Enter employee's name (or type 'Done' to stop): ")
        
        # If the user types "Done", exit the loop
        if employee_name == "done":
            break
        
        # Ask for hours worked and pay rate
        try:
            hours_worked = float(input(f"How many hours did {employee_name} work?"))
            pay_rate = float(input(f"What is {employee_name} pay rate?"))
        except ValueError:
            print("Invalid input. Please enter numeric values for hours worked and pay rate.")
            continue  # Skip the current loop iteration if input is invalid

        # Calculate regular pay, overtime hours, overtime pay, and gross pay
        regular_pay, overtime_hours, overtime_pay, gross_pay = calculate_pay(hours_worked, pay_rate)
        
        # Display the results for the employee
        print(f"\nEmployee Name: {employee_name}")
        
        print(f"Hours Worked: {hours_worked:.2f}")
        print(f"Pay Rate: ${pay_rate:.2f}")
        print(f"Overtime Hours: {overtime_hours:.2f}")
        print(f"Overtime Pay: ${overtime_pay:.2f}")
        print(f"Pay for Regular Hours: ${regular_pay:.2f}")
        print(f"Gross Pay: ${gross_pay:.2f}\n")
        
        # Update the totals
        total_overtime_pay += overtime_pay
        total_regular_pay += regular_pay
        total_gross_pay += gross_pay
        num_employees += 1
    
    # Display the summary after all employees are entered
    if num_employees > 0:
        print(f"Total number of employees entered: {num_employees}")
        print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
        print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
        print(f"Total amount paid in gross: ${total_gross_pay:.2f}")
    else:
        print("\nNo employee data entered.")
        

# Run the program
if __name__ == "__main__":
    main()
