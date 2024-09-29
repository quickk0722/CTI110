"""
Pseudocode for Travel Budget Calculator:
1. Start
2. Prompt user for total budget and store it in 'budget'
3. Prompt user for travel destination and store it in 'destination'
4. Prompt user for gas expense and store it in 'gas_expense'
5. Prompt user for accommodation expense and store it in 'accommodation_expense'
6. Prompt user for food expense and store it in 'food_expense'
7. Calculate total expenses by adding gas_expense, accommodation_expense, and food_expense
8. Calculate remaining budget by subtracting total_expenses from budget
9. Display trip details including:
   - Travel destination
   - Total budget
   - Total expenses
   - Remaining budget
10. If remaining budget is less than 0:
    - Display message indicating user is over budget and by how much
11. Else:
    - Display message indicating user is within budget and how much is left
12. Wait for user to press Enter before exiting
13. End
"""
# Kwadeja Quick
# September 29, 2024
# P1HW2
# A Python program that asks the user for their travel budget, destination,
# and expenses, then calculates the remaining budget after expenses.
print('This program calculates and displays travel expenses')
print("\n")
# Asking the user for inputs
budget = float(input("Enter budget: $"))
print("\n")
destination = input("Enter your travel destination: ")
print("\n")
gas_expense = float(input("How much do you think you will spend on gas?: $"))
print("\n")
accommodation_expense = float(input("Approximately, how much will you need for accomodation/hotel?: $"))
print("\n")
food_expense = float(input("Last, how much do you need for food?: $"))
print("\n")
print('------------Travel Expenses------------')
# Calculating total expenses
total_expenses = gas_expense + accommodation_expense + food_expense

# Calculating remaining budget
remaining_budget = budget - total_expenses

# Show the results
print("\nLocation:", destination)
print("Initial budget: $", budget)
print("\n")
print("Fuel: $", gas_expense)
print("Accomodation: $", accommodation_expense)
print("Food: $", food_expense)
print("\n")
print("Remaining balance: $", remaining_budget)

# Pause before exiting
input("\nPress Enter to exit...")
