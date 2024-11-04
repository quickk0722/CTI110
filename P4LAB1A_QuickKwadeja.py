# Kwadeja Quick
# November 3rd, 2024
# Square and Triangle
import turtle

# Function to draw a square
def draw_square(size):
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)

# Function to draw a triangle
def draw_triangle(size):
    for _ in range(3):
        turtle.forward(size)
        turtle.left(120)

# Draw a square
draw_square(100)

# Move to a new position to draw the triangle
turtle.penup()
turtle.goto(-150, 0)
turtle.pendown() 

# Draw a triangle
draw_triangle(100)

# Finish
turtle.done()
