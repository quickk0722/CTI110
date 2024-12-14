# Kwadeja Quick
# October 12, 2024
# Editing and enhancing exiting programs
# P2HW1

print('This program calculates and displays travel expenses\n')

# Function to safely get float input
def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

# Asking the user for inputs
budget = get_float_input("Enter budget: $")
print()  # Adding spacing

destination = input("Enter your travel destination: ")
print()  # Adding spacing

gas_expense = get_float_input("How much do you think you will spend on gas?: $")
print()  # Adding spacing

accommodation_expense = get_float_input("Approximately, how much will you need for accommodation/hotel?: $")
print()  # Adding spacing

food_expense = get_float_input("Last, how much do you need for food?: $")
print()  # Adding spacing

print('------------Travel Expenses------------')

# Calculating total expenses
total_expenses = gas_expense + accommodation_expense + food_expense

# Calculating remaining budget
remaining_budget = budget - total_expenses

# Show the results with formatted output
print(f"\n{'Location:':<30} {destination}")
print(f"{'Initial budget:':<30} ${budget:.2f}")
print(f"{'Fuel:':<30} ${gas_expense:.2f}")
print(f"{'Accommodation:':<30} ${accommodation_expense:.2f}")
print(f"{'Food:':<30} ${food_expense:.2f}")
print(f"{'Total expenses:':<30} ${total_expenses:.2f}")
print(' -----------------------------------------')
print(f"\n{'Remaining balance:':<30} ${remaining_budget:.2f}")

# Pause before exiting
input("\nPress Enter to exit...")
