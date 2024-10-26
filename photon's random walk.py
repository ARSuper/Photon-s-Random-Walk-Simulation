import turtle as t
import random
import math

# Input the radius of the circle
r = float(input('What is the radius?'))

# Set the turtle's speed to the fastest (0) otherwise we'll be here all day
t.speed(0)

# Initialize the variables!
resultant = 0
step = 5
count = 0
rx = 0
ry = 0
theta_initial = 0

# Lift the pen and move to the starting point
t.penup()
t.forward(r)
t.left(90)
t.pendown()

# Draw a circle with radius 'r' centered at (0, 0)
t.circle(r)

# Lift the pen and move back to the center
t.penup()
t.goto(0, 0)
t.right(90)
t.pendown()

# Simulate the photon's random walk within the circle
while resultant <= r:
    # Generate a random angle in degrees
    theta = random.random() * 360

    # Convert the angle from degrees to radians
    theta_radians = theta * (math.pi / 180)

    # Calculate the x and y components of the step
    x_comp = step * math.cos(theta_radians)
    y_comp = step * math.sin(theta_radians)

    # Update the position components
    rx = rx + x_comp
    ry = ry + y_comp

    # Calculate the resultant distance from the origin
    resultant = math.sqrt(rx ** 2 + ry ** 2)

    # Rotate the turtle by the random angle
    t.left(theta - theta_initial)

    # Move the turtle forward by 'step' units
    t.forward(step)

    # Increment the step count
    count = count + 1

    # Update the initial angle for the next step
    theta_initial = theta

# Print the number of steps taken for the photon to exit the radiative zone
print("The photon took " + str(count) + " steps to exit the radiative zone")
