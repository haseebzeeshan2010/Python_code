# ----- Constants -----
# =====> Create three constants one for each box size




# ----- Variables -----
colour = ""
count = 0

# Get the user input
colour = input ("Which colour (B, R, W)? ")
# =====> Complete the line to convert the entered colour to uppercase
colour = colour.upper()
count = int (input ("How many do you need? "))

# Check for valid inputs
# =====> Complete the line with the required logic operators
if (( not (count <= 0)) and ((colour == "B")  or (colour == "R") or (colour == "W"))):
    # Check to see if count is a whole box
    # =====> Complete the selection statement with relational and logical tests
    if (colour == "B" and (count % 5) == 0):
        print ("Sending " + str(count) + " blue.")
    elif (colour == "R" and (count % 10) == 0):
        print ("Sending " + str (count) + " red.")
    elif (colour == "W" and (count % 8) == 0):
        print ("Sending " + str (count) + " white.")
    else:
        print ("Invalid count")
else:
    print("Invalid input")