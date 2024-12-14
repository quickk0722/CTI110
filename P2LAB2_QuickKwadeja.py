# Kwadeja Quick
# October 6th, 2024
# P2LAB2
# Coding that uses a dictionary to store user input and displays output to the user
                         
# Create a dictionary to store automobile MPG values
mpg_dict = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

# Create a variable to hold all the keys from the dictionary
keys = mpg_dict.keys()

# Display the available vehicles to the user
print("Available vehicles:")
for key in keys:
    print(key)

# Prompt the user to enter a vehicle
vehicle = input("\nEnter a vehicle to see it's mpg: ")

# Check if the vehicle is in the dictionary
if vehicle in mpg_dict:
    # Display the MPG for the entered vehicle
    mpg = mpg_dict[vehicle]
    print(f"{vehicle} has {mpg} MPG.")

    # Prompt the user for the number of miles they will drive
    miles = float(input("How many miles you will drive: "))

    # Calculate gallons of gas needed
    gallons_needed = miles / mpg

    # Display the gallons needed, rounded to two decimal places
    print(f"You will need approximately {gallons_needed:.2f} gallons of gas.")
else:
    print("Sorry, that vehicle is not in the list. Please ensure you typed it correctly.")
