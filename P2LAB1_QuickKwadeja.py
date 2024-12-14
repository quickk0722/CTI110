# Kwadeja Quick
# October 6th, 2024
# P2LAB1
# Coding that performs variables and expressions 

import math

def main():
    # Get radius input from user
    radius = float(input("What is the radius of the circle: "))
    
    # Calculate diameter, circumference, and area
    diameter = 2 * radius
    circumference = 2 * math.pi * radius
    area = math.pi * radius ** 2
    
    # Display the results with specified formatting
    print(f"The diameter of the circle is: {diameter:.1f}")
    print(f"The circumference of the circle is: {circumference:.2f}")
    print(f"The area of the circle is: {area:.3f}")

    # Pause before exiting
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()


