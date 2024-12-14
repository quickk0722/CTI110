# Kwadeja Quick
# October 13, 2024
# P2HW2
# Grade Calculator
"""
Pseudocode for Grade Calculator Program:
1. Start
2. Initialize an empty list called 'grades'
3. For each module from 1 to 6:
    a. Prompt the user to enter the grade for the current module
    b. Convert the entered grade to float and append it to the 'grades' list
4. Calculate the lowest grade using the min() function
5. Calculate the highest grade using the max() function
6. Calculate the sum of grades using the sum() function
7. Calculate the average of grades by dividing the sum by the number of grades
8. Display the following information:
    a. The lowest grade
    b. The highest grade
    c. The sum of grades
    d. The average of grades formatted to two decimal places
9. End
"""

# Initialize an empty list for grades
grades = []

# Get grades for each module
module = 1
while module <= 6:
    grade = float(input(f"Enter grade for Module {module}: "))
    grades.append(grade)
    module += 1

# Calculate the lowest grade
lowest_grade = min(grades)

# Calculate the highest grade
highest_grade = max(grades)

# Calculate the sum of grades
sum_of_grades = sum(grades)

# Calculate the average of grades
average_grade = sum_of_grades / len(grades)

# Results
# print () Adding spacing

print('------------- Results---------------')
print(f'\nLowest Grade:         {lowest_grade}')
print(f'Highest Grade:        {highest_grade}')
print(f'Sum of Grades:        {sum_of_grades}')
print(f'Average Grade:        {average_grade:.2f}')
print('---------------------------------------')
