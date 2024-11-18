# Kwadeja Quick
# P5LAB
# November 17, 2024
# Use of loops, functions and module import to complete assignments

import random

def calculate_coins(amount):
    # Convert amount to cents
    cents = int(amount * 100)
    
    # Coin values in cents
    dollar_value = 100
    quarter_value = 25
    dime_value = 10
    nickel_value = 5
    penny_value = 1
    
    # Calculate the number of each coin type
    dollars = cents // dollar_value
    cents %= dollar_value
    
    quarters = cents // quarter_value
    cents %= quarter_value
    
    dimes = cents // dime_value
    cents %= dime_value
    
    nickels = cents // nickel_value
    cents %= nickel_value
    
    pennies = cents // penny_value
    
    # Prepare the change as a list of strings to print vertically
    change_list = []
    
    if dollars > 0:
        change_list.append(f"{dollars} dollar{'s' if dollars > 1 else ''}")
    if quarters > 0:
        change_list.append(f"{quarters} quarter{'s' if quarters > 1 else ''}")
    if dimes > 0:
        change_list.append(f"{dimes} dime{'s' if dimes > 1 else ''}")
    if nickels > 0:
        change_list.append(f"{nickels} nickel{'s' if nickels > 1 else ''}")
    if pennies > 0:
        change_list.append(f"{pennies} penn{'ies' if pennies > 1 else 'y'}")
    
    return change_list

def main():
    # Generate a random float value for the total owed (between 1.00 and 100.00)
    total_owed = round(random.uniform(1.00, 100.00), 2)
    print(f"The total amount owed is: ${total_owed}")
    
    valid_input = False
    
    while not valid_input:
        user_input = input("Enter the amount of money you will put into the machine: $")
        
        try:
            money_inserted = float(user_input)
            
            if money_inserted < total_owed:
                print(f"Sorry, you need to insert at least ${total_owed}. Please try again.")
            else:
                change_due = money_inserted - total_owed
                print(f"Change due: ${round(change_due, 2)}")
                
                # Calculate the coins for the change
                if change_due > 0:
                    result = calculate_coins(change_due)
                    print("Your change will be:")
                    for line in result:
                        print(line)  # Print each coin type on a new line
                else:
                    print("No change needed!")
                valid_input = True
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Run the program
if __name__ == "__main__":
    main()
