# -------------------------------------------------------------------
# Import libraries
# -------------------------------------------------------------------

# ===> Complete this line to import the random library
import random

# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------

# ===> Create an integer variable named roll and set it to 0
roll = 0

# ===> Create a constant named SIDES and set it to 6
SIDES = 6

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

# ===> Assign the result of this library call to the variable roll
roll = random.randint(1, SIDES)

# ===> Display the message "Your roll is" and the variable roll

print("Your roll is ", roll)