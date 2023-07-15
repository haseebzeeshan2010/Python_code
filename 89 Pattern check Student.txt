# ------------------------------------------------------------
# Constants
# ------------------------------------------------------------
SPECIAL = ["%", "&", "$", "@"]

# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
# Any combination of digits and letters, plus exactly one
#     special symbol at any location.  It must be exactly
#     nine characters long.
passKey = "1234*ABCD"
temp = ""

# ------------------------------------------------------------
# Subprograms
# ------------------------------------------------------------
def locateSpecial (pKey):
    location = -1
    index = 0

    # =====> Check each special character until found or end of specials
    while ((index               ) and (location               )):
        # =====> Complete the line to identify the location of the
        #        special symbol, if there is one
        location = pKey.find (               )
        index = index + 1

    return (location)

# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
passKey = input ("Enter your pass key: ")

# Check overall length first
if (len (passKey) == 9):

    # Check for location of special character
    # =====> Complete the line to call the locateSpecial subprogram
    symbolLocation =

    if (symbolLocation != -1):
        # Copy all characters, except symbol to temporary variable
        # =====> Complete the values for the range() function to
        #        copy all characters before the special symbol
        #        to a temporary variable
        for index in range (               ):
            temp = temp + passKey[index]

        # =====> Complete the values for the range() function to
        #        copy all characters after the special symbol
        #        to a temporary variable
        for index in range (               ):
            temp = temp + passKey[index]

        # Check for all aphanumeric values
        # =====> Complete the line to check for all alphanumeric values
        if (               ):
            print (passKey + " is valid")
        else:
            print ("Disallowed character found")
    else:
        print ("Must have one of %&$@ symbols")
else:
    print ("Invalid length")
