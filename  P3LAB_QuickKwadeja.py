# Kwadeja Quick
# October 19, 2024
# CTI 110
# Code that displays information to users

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
    
    # Output
    output = []
    
    if dollars > 0:
        output.append(f"{dollars} dollar{'s' if dollars > 1 else ''}")
    if quarters > 0:
        output.append(f"{quarters} quarter{'s' if quarters > 1 else ''}")
    if dimes > 0:
        output.append(f"{dimes} dime{'s' if dimes > 1 else ''}")
    if nickels > 0:
        output.append(f"{nickels} nickel{'s' if nickels > 1 else ''}")
    if pennies > 0:
        output.append(f"{pennies} penn{'ies' if pennies > 1 else 'y'}")
    
    return ', '.join(output)

# Main program
valid_input = False

while not valid_input:
    user_input = input("Enter the amount of money as a float: ")
    
    # Check if the input can be converted to float
    if user_input.replace('.', '', 1).isdigit():
        money = float(user_input)
        if money == 0.00:
            print("No change")
        else:
            result = calculate_coins(money)
            print(f"{result}")
            valid_input = True
    else:
        print("Invalid input. Please enter a valid number.")
