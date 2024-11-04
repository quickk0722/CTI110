# Kwadeja Quick
# November 3rd, 2024
# Program Running with positive integer input


def multiplication_table(n):
    print(f"\nMultiplication table for {n}:")
    for i in range(1, 13):
        print(f"{n} x {i} = {n * i}")

def main():
    while True:
        user_input = input("Please enter an integer: ")
        
        try:
            number = int(user_input)
            if number < 0:
                print("Negative values are not accepted.")
            else:
                multiplication_table(number)

        except ValueError:
            print("That's not an integer. Please try again.")

        again = input("Would you like to run the program again? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
