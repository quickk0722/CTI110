# Kwadeja Quick
# October 20, 2024
# Debug


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# Add grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# Determine lowest, highest , sum and average for grades

lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
average_grade = sum_of_grades / len(grades)

print('------------- Results---------------')
print(f'\nLowest Grade:         {lowest_grade}')
print(f'Highest Grade:        {highest_grade}')
print(f'Sum of Grades:        {sum_of_grades}')
print(f'Average Grade:        {average_grade:.2f}')
print('---------------------------------------')

# Determine letter grade for average
if average_grade >= 90:
 print('Your grade is: A')
elif average_grade >= 80:
 print('Your grade is: B')
elif average_grade >= 70:
 print('Your grade is: C')
elif average_grade >= 60:
 print('Your grade is: D')
else:
 print('Your grade is: F')

 





