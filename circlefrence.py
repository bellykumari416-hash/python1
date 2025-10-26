import math

# Get the radius from the user
try:
    radius = float(input("Enter the radius of the circle: "))
except ValueError:
    print("Invalid input. Please enter a number for the radius.")
    exit()

# Calculate the circumference
circumference = 2 * math.pi * radius

# Display the result
print(f"The circumference of the circle with radius {radius} is: {circumference:.2f}")