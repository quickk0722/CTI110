# Kwadeja Quick
# November 3rd, 2024
# Initials

import turtle

# Set up the turtle
t = turtle.Turtle()
t.color("orange")
t.pensize(3)

# Function to draw the letter 'K'
t.left(90)
t.forward(100)
t.backward(50)
t.right(45)
t.forward(70)
t.backward(70)
t.right(90)
t.forward(70)
t.backward(70)

# Move to draw next letter
t.penup()
t.forward(100)
t.left(50)
t.pendown()

# Function to draw the letter 'Q'
t.circle(50, 360)
t.forward(50)
t.backward(50)

turtle.done()  # Keep the window open
