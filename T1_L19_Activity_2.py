# ---------------------------------------------------------
# Variables
# ---------------------------------------------------------
quote = "Computer science is my favourite subject."

# ---------------------------------------------------------
# Main program
# ---------------------------------------------------------
# Get the inputs
firstName = input ("Enter your first name ")
numInput = int (input ("Enter a number between 1 and 10 "))

# =====> Complete the statement to check if the name is too short
if (len (firstName) <= 3):
    print ("The name is not long enough")
# =====> Complete the statement to check if the number is less than 0
elif (numInput < 1):
    print ("The number is too low")
# =====> Complete the statement to check if the number is greater than 10
elif (numInput > 10):
    print ("The number is too high")
# Otherwise, do the processing
else:
    # =====> Convert the name to uppercase
    firstName = firstName.upper ()
    # =====> Calculate the new number
    newNum = numInput * 123

    # =====> Create a ticket ID, using indexing, len(), str(), and concatenation
    ticket = firstName[0] + firstName[len(firstName) - 1] + str (newNum)

    # Display the result using slicing and concatenation
    print ("The " + quote[9:16] + " ticket is " + ticket)