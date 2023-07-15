# Calculate the circumference of a circle,
#      the area of a circle,
#      and the volume of a sphere

# Set constants
MY_PI = 3.14159         # Approximate

# Set variables
radius = 12.75

# Calculate
circumference = 2 * MY_PI * radius
area = MY_PI * radius ** 2
volume = (4 / 3) * MY_PI * radius ** 3

# Display results
circumference = round (circumference, 2)
print (circumference)

print (round (area, 4))     # Nest the code
print (round (volume, 6))