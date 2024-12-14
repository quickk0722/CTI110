# Kwadeja Quick
# November 24, 2024
# P5HW
# Use of loops, functions and module import to complete a program
import random

# Function to generate random numbers and ask for addition answer
def add_numbers():
    num1 = random.randint(1, 1000)
    num2 = random.randint(1, 1000)
    correct_answer = num1 + num2
    
    print(f"\n{num1}")
    print(f"+ {num2}")
    
    guesses = 0
    while True:
        try:
            user_answer = int(input("What is the sum? "))
            guesses += 1
            
            if user_answer == correct_answer:
                print(f"Congratulations!!!! Your answer is correct. Number of guesses: {guesses}")
                break  # Correct answer, exit the loop and return to the main menu
            elif user_answer < correct_answer:
                print("Sorry, guess is too low.")
            else:
                print("Sorry, guess is too high.")
        except ValueError:
            print("Please enter a valid integer.")

# Function to generate random numbers and ask for subtraction answer
def subtract_numbers():
    num1 = random.randint(1, 1000)
    num2 = random.randint(1, 1000)
    correct_answer = num1 - num2
    
    print(f"\n{num1}")
    print(f"- {num2}")
    
    guesses = 0
    while True:
        try:
            user_answer = int(input("What is the remainder? "))
            guesses += 1
            
            if user_answer == correct_answer:
                print(f"Congratulations!!!! Your answer is correct. Number of guesses: {guesses}")
                break  # Correct answer, exit the loop and return to the main menu
            elif user_answer < correct_answer:
                print("Sorry, guess is too low.")
            else:
                print("Sorry, guess is too high.")
        except ValueError:
            print("Please enter a valid integer.")

# Function to display the menu and get user choice
def display_menu():
    print("\nWelcome to Math Quiz")
    print("MAIN MENU")
    print("--------------------------")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")

def main():
    while True:
        display_menu()
        
        try:
            choice = int(input("Please choose one of the menu options: "))
            
            if choice == 1:
                add_numbers()  # Calls add_numbers function
            elif choice == 2:
                subtract_numbers()  # Calls subtract_numbers function
            elif choice == 3:
                print("Goodbye!")
                break  # Exit the program
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")

# Call the main function to run the program
if __name__ == "__main__":
    main()

