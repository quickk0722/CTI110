# Kwadeja Quick
# November 09, 2024
# P4HW1
# Ability to edit and enhance exiting programs
"""
Pseudocode:

1. Ask the user how many test scores they would like to enter.
   - If the input is invalid (not an integer or less than 1), prompt the user again.
2. Initialize an empty list to store the test scores.
3. For each score (from 1 to the number entered by the user):
    a. Prompt the user to enter a score.
    b. Check if the entered score is valid (between 0 and 100).
       - If the score is not valid, notify the user and ask for a valid score again.
       - If the score is valid, append it to the list of scores.
4. After collecting all the scores:
    a. Find the lowest score in the list.
    b. Remove the lowest score from the list.
5. Calculate the average of the remaining scores in the list.
6. Display:
    a. The lowest score that was entered.
    b. The modified score list after dropping the lowest score.
    c. The average score (after dropping the lowest).
7. Determine the letter grade based on the average score.
8. Display the letter grade.
9. End Program
"""
def get_valid_score():
    """Helper function to get a valid score between 0 and 100."""
    while True:
        try:
            score = float(input("Enter a score between 0 and 100: "))
            if 0 <= score <= 100:
                return score
            else:
                print("INVALID score entered!!!! Score should be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_letter_grade(average):
    """Function to determine the letter grade based on the average score."""
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def main():
    # Ask user for the number of scores they would like to enter
    while True:
        try:
            num_scores = int(input("How many scores do you want to enter? "))
            if num_scores > 0:
                break
            else:
                print("The number of scores must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter an integer value.")

    # Collect scores in a list
    scores = []
    for i in range(num_scores):
        print(f"Enter score {i + 1}:")
        score = get_valid_score()
        scores.append(score)
        
    # Results
    print ('------Results--------------------------------------------------')
    # Display lowest score
    lowest_score = min(scores)
    print(f"Lowest score: {lowest_score}")

    # Remove the lowest score and calculate average of remaining scores
    scores.remove(lowest_score)

    # Calculate the average of the remaining scores
    average_score = sum(scores) / len(scores)
    print(f"Modified List: {scores}")
    print(f"Average score: {average_score:.2f}")

    # Determine the letter grade
    letter_grade = get_letter_grade(average_score)
    print(f"Letter grade: {letter_grade}")
    print ('---------------------------------------------------------------')
# Run the program
if __name__ == "__main__":
    main()
